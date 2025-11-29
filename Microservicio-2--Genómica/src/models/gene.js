const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Gene = sequelize.define('Gene', {
    id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    symbol: { type: DataTypes.STRING, allowNull: false, unique: true },
    fullName: { type: DataTypes.STRING },
    functionSummary: { type: DataTypes.TEXT }
});

module.exports = Gene;