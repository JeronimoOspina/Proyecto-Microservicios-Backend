const Gene = require('../models/gene');
const Variant = require('../models/variant');
const PatientReport = require('../models/PatientReport');
const { checkPatientExists } = require('../services/clinicService');

// --- GENES ---
exports.createGene = async (req, res) => {
    try {
        const gene = await Gene.create(req.body);
        res.status(201).json(gene);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

exports.getGenes = async (req, res) => {
    const genes = await Gene.findAll();
    res.json(genes);
};

// --- VARIANTES ---
exports.createVariant = async (req, res) => {
    try {
        const variant = await Variant.create(req.body);
        res.status(201).json(variant);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};


exports.createPatientReport = async (req, res) => {
    const { patientId, variantId, alleleFrequency } = req.body;

    try {

        const variant = await Variant.findByPk(variantId);
        if (!variant) {
            return res.status(404).json({ message: 'Variante genética no encontrada' });
        }

        const patientData = await checkPatientExists(patientId);
        
        if (!patientData) {
            return res.status(404).json({ message: `El paciente con ID ${patientId} no existe en Clínica.` });
        }

        const report = await PatientReport.create({
            patientId,
            variantId,
            alleleFrequency
        });

        res.status(201).json({
            message: "Reporte creado exitosamente",
            reportId: report.id,

            patientContext: {
                fullName: `${patientData.first_name} ${patientData.last_name}`,
                status: patientData.status
            }
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};