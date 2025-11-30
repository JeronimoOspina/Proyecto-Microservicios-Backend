const axios = require('axios');

const checkPatientExists = async (patientId) => {
    try {

        const url = `${process.env.CLINIC_SERVICE_URL}/pacientes/${patientId}`;
        console.log(`[Genómica] Consultando paciente en: ${url}`);
        
        const response = await axios.get(url);
        
        
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 404) {
            console.warn(`[Genómica] Paciente ${patientId} no encontrado.`);
            return null; // El paciente no existe
        }
        console.error(`Error conectando con Clínica: ${error.message}`);
        throw new Error("Servicio de Clínica no disponible");
    }
};

module.exports = { checkPatientExists };