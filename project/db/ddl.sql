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

CREATE TABLE PROPRIETARIO(
idProprietario INT NOT NULL,
email VARCHAR(50) NOT NULL,
nomeCompleto VARCHAR(100) NOT NULL,
senha VARCHAR(50) NOT NULL,
CONSTRAINT PROPRIETARIO_PK PRIMARY KEY(idProprietario)
);

CREATE TABLE FUNCIONARIO (
idFuncionario INT NOT NULL,
nomeCompleto VARCHAR(100) NOT NULL,
senha VARCHAR(50) NOT NULL,
idProprietario INT NOT NULL,
CONSTRAINT FUNCIONARIO_PK PRIMARY KEY(idFuncionario),
CONSTRAINT FUNCIONARIO_PROPRIETARIO_FK FOREIGN KEY (idProprietario)
REFERENCES PROPRIETARIO(idProprietario)
);

CREATE TABLE FAZENDA (
idFazenda INT NOT NULL,
tamanhoFazenda INT NOT NULL,
idProprietario INT NOT NULL,
CONSTRAINT FAZENDA_PK PRIMARY KEY (idFazenda),
CONSTRAINT FAZENDA_PROPRIETARIO_FK FOREIGN KEY (idProprietario)
REFERENCES PROPRIETARIO(idProprietario)
);

CREATE TABLE trabalha (
idFuncionario INT NOT NULL,
idFazenda INT NOT NULL,
CONSTRAINT trabalha_FUNCIONARIO_FK FOREIGN KEY (idFuncionario)
REFERENCES FUNCIONARIO(idFuncionario),
CONSTRAINT trabalha_FAZENDA_FK FOREIGN KEY (idFazenda)
REFERENCES FAZENDA(idFazenda)
);