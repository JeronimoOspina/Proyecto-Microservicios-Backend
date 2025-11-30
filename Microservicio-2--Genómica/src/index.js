const express = require('express');
const sequelize = require('./config/database');
const genomicsRoutes = require('./routes/genomicsRoutes');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

app.use('/api/v1/genomics', genomicsRoutes);


app.get('/health', (req, res) => res.json({ status: 'ok', service: 'Genomics (Node.js)' }));


sequelize.sync({ force: false }) 
    .then(() => {
        console.log('Tablas sincronizadas con MySQL');
        app.listen(PORT, () => {
            console.log(`Microservicio Genómica corriendo en puerto ${PORT}`);
        });
    })
    .catch(err => {
        console.error(' Error al conectar con la BD:', err);
    });