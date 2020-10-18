-- -------- << iGado Database >> ------------
--
-- SCRIPT DE CRIACAO (DDL)
--
-- Data Criacao ...........: 12/10/2020
-- Autor(es) ..............: Todos
-- Banco de Dados .........: XXX
-- Banco de Dados(nome) ...: iGado
--
-- Data Ultima Alteracao ..: 12/10/2020
-- => Criação do modelo físico do banco de dados com tabelas iniciais
--
-- PROJETO => 01 Base de Dados
-- => 09 Tabelas
-------------------------------------------------------------------

CREATE TABLE OWNER(
idOwner INT NOT NULL,
email VARCHAR(50) NOT NULL,
fullName VARCHAR(100) NOT NULL,
password VARCHAR(50) NOT NULL,
CONSTRAINT OWNER_PK PRIMARY KEY(idOwner)
);

CREATE TABLE EMPLOYEE (
idEmployee INT NOT NULL,
fullName VARCHAR(100) NOT NULL,
password VARCHAR(50) NOT NULL,
idOwner INT NOT NULL,
CONSTRAINT EMPLOYEE_PK PRIMARY KEY(idEmployee),
CONSTRAINT EMPLOYEE_OWNER_FK FOREIGN KEY (idOwner)
REFERENCES OWNER(idOwner)
);

CREATE TABLE FARM (
idFarm INT NOT NULL,
sizeFarm INT NOT NULL,
idOwner INT NOT NULL,
CONSTRAINT FARM_PK PRIMARY KEY (idFarm),
CONSTRAINT FARM_OWNER_FK FOREIGN KEY (idOwner)
REFERENCES OWNER(idOwner)
);

CREATE TABLE work (
idEmployee INT NOT NULL,
idFarm INT NOT NULL,
CONSTRAINT work_EMPLOYEE_FK FOREIGN KEY (idEmployee)
REFERENCES EMPLOYEE(idEmployee),
CONSTRAINT work_FARM_FK FOREIGN KEY (idFarm)
REFERENCES FARM(idFarm)
);