1. Health Check
GET /health

Verifica que el servicio esté activo.

Respuesta ejemplo:

{
  "status": "ok"
}


2. Autenticación
POST /login

Genera un token JWT para acceder a las rutas protegidas.
{
  "email": "paciente12345@gmail"
}


3. Gestión de Pacientes
3.1 Crear Paciente

POST /pacientes/
Headers:
Authorization: Bearer <token>
{
  "first_name": "Marcelo",
  "last_name": "Agacha teconocelo",
  "birth_date": "1990-05-10",
  "gender": "M"
}

3.2 Obtener Paciente por ID
GET /pacientes/{id}
Ejemplo:
GET /pacientes/1

3.3 Actualizar Paciente
PUT /pacientes/{id}
Body:
{
  "first_name": "Juan",
  "last_name": "Perez",
  "birth_date": "1990-01-01",
  "gender": "M"
}

4. Tipos de Tumor
4.1 Obtener todos los tumores
GET /tumores/
Requiere token de autenticación.

4.2 Crear tipo de tumor
POST /tumores/
Body:
{
  "name": "Tumor 2",
  "system_affected": "Nervioso"
}

5. Historias Clínicas
5.1 Registrar nueva historia clínica
POST /historias/
Body:
{
  "patient_id": 1,
  "tumor_type_id": 2,
  "diagnosis_date": "2025-11-30",
  "stage": "II",
  "treatment_protocol": "Quimioterapia"
}

5.2 Obtener historias por paciente
GET /historias/paciente/{id}
GET /historias/paciente/1

6. Genes
6.1 Crear gen
POST /genes
Body:
{
  "symbol": "BRCA123",
  "fullName": "Breast Cancer 1",
  "functionSummary": "DNA repair gene"
}

6.2 Obtener lista de genes
GET /genes

7. Variantes Genéticas
7.1 Crear variante genética
POST /variants
Body:
{
  "chromosome": "17",
  "position": 41276045,
  "referenceBase": "A",
  "alternateBase": "G",
  "impact": "High",
  "geneId": 1
}

8. Reportes Clínicos / Genómicos
8.1 Crear reporte
POST /reports
{
  "patientId": 1,
  "variantId": "a6525dc7-4a54-4d45-9cf0-d0997fed771c",
  "alleleFrequency": 0.45
}
