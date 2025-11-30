const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const Gene = require('./gene');

const Variant = sequelize.define('Variant', {
    id: { type: DataTypes.UUID, defaultValue: DataTypes.UUIDV4, primaryKey: true },
    chromosome: { type: DataTypes.STRING, allowNull: false },
    position: { type: DataTypes.INTEGER, allowNull: false },
    referenceBase: { type: DataTypes.STRING },
    alternateBase: { type: DataTypes.STRING },
    impact: { type: DataTypes.STRING }
});


Variant.belongsTo(Gene, { foreignKey: 'geneId' });
Gene.hasMany(Variant, { foreignKey: 'geneId' });

module.exports = Variant;