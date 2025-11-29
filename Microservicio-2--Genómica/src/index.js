const express = require('express');
const sequelize = require('./config/database');
const genomicsRoutes = require('./routes/genomicsRoutes');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Rutas base
app.use('/api/v1/genomics', genomicsRoutes);

// Health Check
app.get('/health', (req, res) => res.json({ status: 'ok', service: 'Genomics (Node.js)' }));

// Sincronización de BD y arranque
// force: false evita borrar los datos cada vez que reinicias
sequelize.sync({ force: false }) 
    .then(() => {
        console.log('✅ Tablas sincronizadas con MySQL');
        app.listen(PORT, () => {
            console.log(`🚀 Microservicio Genómica corriendo en puerto ${PORT}`);
        });
    })
    .catch(err => {
        console.error('❌ Error al conectar con la BD:', err);
    });