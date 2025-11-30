package main

import (
	"bytes"
	"io"
	"log"
	"net/http"
	"net/mail"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"
	"github.com/joho/godotenv"
)

var jwtSecret []byte
var clinicURL string
var genomicsURL string

func init() {
	err := godotenv.Load()
	if err != nil {
		log.Println("No .env file found, usando variables de entorno del sistema")
	}
	jwtSecret = []byte(os.Getenv("JWT_SECRET"))
	clinicURL = os.Getenv("CLINIC_SERVICE_URL")       // http://clinica:8001/api/v1
	genomicsURL = os.Getenv("GENOMICS_SERVICE_URL")  // http://genomica:3001/api/v1/genomics
}

func main() {
	r := gin.Default()

	// Login
	r.POST("/login", loginHandler)

	// Rutas proxy con autenticación
	auth := r.Group("/", authMiddleware())
	{
		// Clínica
		auth.Any("/pacientes/*path", func(c *gin.Context) {
			clinicProxy(c, "/pacientes")
		})
		auth.Any("/tumores/*path", func(c *gin.Context) {
			clinicProxy(c, "/tumores")
		})
		auth.Any("/historias/*path", func(c *gin.Context) {
			clinicProxy(c, "/historias")
		})

		// Genómica
		auth.Any("/genes/*path", func(c *gin.Context) {
			genomicsProxy(c, "/genes")
		})
		auth.Any("/variants/*path", func(c *gin.Context) {
			genomicsProxy(c, "/variants")
		})
		auth.Any("/reports/*path", func(c *gin.Context) {
			genomicsProxy(c, "/reports")
		})
	}

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok", "service": "API Gateway"})
	})

	r.Run(":8080")
}

// ======================
// HANDLERS
// ======================

func loginHandler(c *gin.Context) {
	type LoginRequest struct {
		Email string `json:"email"`
	}

	var req LoginRequest
	if err := c.BindJSON(&req); err != nil || req.Email == "" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Correo requerido"})
		return
	}

	// Validar formato de email
	if _, err := mail.ParseAddress(req.Email); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Formato de correo inválido"})
		return
	}

	// Generar token
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"email": req.Email,
		"role":  "user",
		"exp":   time.Now().Add(time.Hour * 24).Unix(),
	})

	tokenString, err := token.SignedString(jwtSecret)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "No se pudo generar token"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"token": tokenString})
}

func authMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		authHeader := c.GetHeader("Authorization")
		if authHeader == "" {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Authorization header requerido"})
			return
		}

		if len(authHeader) < 7 || authHeader[:7] != "Bearer " {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Formato de token inválido"})
			return
		}

		tokenString := authHeader[7:]
		token, err := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
			return jwtSecret, nil
		})
		if err != nil || !token.Valid {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Token inválido"})
			return
		}

		c.Next()
	}
}

// ======================
// PROXY
// ======================

func clinicProxy(c *gin.Context, prefix string) {
	path := c.Param("path")
	url := clinicURL + prefix + path
	proxyRequest(c, url)
}

func genomicsProxy(c *gin.Context, prefix string) {
	path := c.Param("path")
	url := genomicsURL + prefix + path
	proxyRequest(c, url)
}

func proxyRequest(c *gin.Context, url string) {
	client := &http.Client{}
	method := c.Request.Method

	var body io.Reader
	if c.Request.Body != nil {
		buf := new(bytes.Buffer)
		_, _ = buf.ReadFrom(c.Request.Body)
		body = buf
	}

	req, err := http.NewRequest(method, url, body)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// Copiar headers originales
	for k, v := range c.Request.Header {
		req.Header[k] = v
	}

	resp, err := client.Do(req)
	if err != nil {
		c.JSON(http.StatusServiceUnavailable, gin.H{"error": err.Error()})
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	c.Data(resp.StatusCode, resp.Header.Get("Content-Type"), respBody)
}
