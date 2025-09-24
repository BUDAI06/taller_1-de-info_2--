CREATE DATABASE hospital;
USE hospital;

CREATE TABLE sensores (
    id_sensor VARCHAR(20) PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    unidad_medida VARCHAR(20) NOT NULL,
    atributo_extra VARCHAR(100)
);
