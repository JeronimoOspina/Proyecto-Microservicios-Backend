const express = require('express');
const router = express.Router();
const controller = require('../controllers/genomicsController');

// Genes
router.post('/genes', controller.createGene);
router.get('/genes', controller.getGenes);

// Variantes
router.post('/variants', controller.createVariant);

// Reportes (Aquí probamos la conexión entre microservicios)
router.post('/reports', controller.createPatientReport);

module.exports = router;