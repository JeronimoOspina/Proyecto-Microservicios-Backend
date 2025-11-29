const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const Variant = require('./variant');

const PatientReport = sequelize.define('PatientReport', {
    id: { type: DataTypes.UUID, defaultValue: DataTypes.UUIDV4, primaryKey: true },

    patientId: { type: DataTypes.INTEGER, allowNull: false }, 
    detectionDate: { type: DataTypes.DATE, defaultValue: DataTypes.NOW },
    alleleFrequency: { type: DataTypes.DECIMAL(5, 4) }
});

// Relación con Variante
PatientReport.belongsTo(Variant, { foreignKey: 'variantId' });

module.exports = PatientReport;