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

CREATE TABLE _USER(
    idUser INT NOT NULL,
    email VARCHAR(50) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    isProprietary BOOLEAN NOT NULL,
    CONSTRAINT _USER_PK PRIMARY KEY(idUser)
);

CREATE TABLE FARM (
    idFarm INT NOT NULL,
    sizeFarm INT NOT NULL,
    idUser INT NOT NULL,
    CONSTRAINT FARM_PK PRIMARY KEY (idFarm),
    CONSTRAINT FARM_USER_FK FOREIGN KEY (idUser)
    REFERENCES _USER(idUser)
);

CREATE TABLE work (
    idUser INT NOT NULL,
    idFarm INT NOT NULL,
    CONSTRAINT work_USER_FK FOREIGN KEY (idUser)
    REFERENCES _USER(idUser),
    CONSTRAINT work_FARM_FK FOREIGN KEY (idFarm)
    REFERENCES FARM(idFarm)
);