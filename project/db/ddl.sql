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

CREATE TABLE PROPRIETARY(
idProprietary INT NOT NULL,
email VARCHAR(50) NOT NULL,
fullName VARCHAR(100) NOT NULL,
password VARCHAR(50) NOT NULL,
CONSTRAINT PROPRIETARY_PK PRIMARY KEY(idProprietary)
);

CREATE TABLE EMPLOYEE (
idEmployee INT NOT NULL,
fullName VARCHAR(100) NOT NULL,
password VARCHAR(50) NOT NULL,
idProprietary INT NOT NULL,
CONSTRAINT EMPLOYEE_PK PRIMARY KEY(idEmployee),
CONSTRAINT EMPLOYEE_PROPRIETARY_FK FOREIGN KEY (idProprietary)
REFERENCES PROPRIETARY(idProprietary)
);

CREATE TABLE FARM (
idFarm INT NOT NULL,
sizeFarm INT NOT NULL,
idProprietary INT NOT NULL,
CONSTRAINT FARM_PK PRIMARY KEY (idFarm),
CONSTRAINT FARM_PROPRIETARY_FK FOREIGN KEY (idProprietary)
REFERENCES PROPRIETARY(idProprietary)
);

CREATE TABLE work (
idEmployee INT NOT NULL,
idFarm INT NOT NULL,
CONSTRAINT work_EMPLOYEE_FK FOREIGN KEY (idEmployee)
REFERENCES EMPLOYEE(idEmployee),
CONSTRAINT work_FARM_FK FOREIGN KEY (idFarm)
REFERENCES FARM(idFarm)
);