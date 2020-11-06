-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.

CREATE TABLE Contato_Emergencia (
telefone  VARCHAR(255),
id_emergencia SERIAL PRIMARY KEY,
nome VARCHAR(255),
id_atleta SERIAL
);

CREATE TABLE Doenca  (
descricao VARCHAR(255),
id_doenca SERIAL PRIMARY KEY
);

CREATE TABLE Medicamento  (
id_medicamento SERIAL PRIMARY KEY,
nome VARCHAR(255),
dose VARCHAR(255)
);

CREATE TABLE Efeito_Colateral  (
id_efeito SERIAL PRIMARY KEY,
descricao VARCHAR(255)
);

CREATE TABLE Projeto  (
id_projeto SERIAL PRIMARY KEY,
descricao  VARCHAR(255),
data TIMESTAMP
);

CREATE TABLE Alergia  (
descricao  VARCHAR(255),
id_alergia SERIAL PRIMARY KEY
);

CREATE TABLE Diretoria  (
id_diretoria SERIAL PRIMARY KEY,
cargo  VARCHAR(255),
id_atleta SERIAL
);

CREATE TABLE atleta_medicamento  (
id_atleta SERIAL,
id_medicamento SERIAL,
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento)
);

CREATE TABLE medicamento_efeitocolateral (
id_medicamento SERIAL,
id_efeito SERIAL,
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento),
FOREIGN KEY(id_efeito) REFERENCES Efeito_Colateral  (id_efeito)
);

CREATE TABLE atleta_alergia (
id_atleta SERIAL,
id_alergia SERIAL,
FOREIGN KEY(id_alergia ) REFERENCES Alergia  (id_alergia)
);

CREATE TABLE Evento  (
local  VARCHAR(255),
id_evento SERIAL PRIMARY KEY,
data TIMESTAMP,
descricao  VARCHAR(255)
);

CREATE TABLE Fluxo_Caixa (
id_fluxo SERIAL PRIMARY KEY,
descricao  VARCHAR(255),
valor  NUMERIC(10),
flag_entrada_saida NUMERIC(10),
data TIMESTAMP
);

CREATE TABLE evento_fluxocaixa (
id_fluxo SERIAL,
id_evento SERIAL,
FOREIGN KEY(id_fluxo ) REFERENCES Fluxo_Caixa (id_fluxo),
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE atleta_fluxocaixa (
id_atleta SERIAL,
id_fluxo SERIAL,
FOREIGN KEY(id_fluxo ) REFERENCES Fluxo_Caixa (id_fluxo)
);

CREATE TABLE Falta  (
id_falta SERIAL PRIMARY KEY,
descricao  VARCHAR(255),
data TIMESTAMP,
id_atleta SERIAL
);

CREATE TABLE doenca_atleta (
id_atleta SERIAL,
id_doenca SERIAL,
FOREIGN KEY(id_doenca ) REFERENCES Doenca  (id_doenca)
);

CREATE TABLE atleta_evento_posicao (
id_atleta SERIAL,
id_evento SERIAL,
id_posicao SERIAL,
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE diretoria_projeto (
id_diretoria SERIAL,
id_projeto SERIAL,
FOREIGN KEY(id_diretoria ) REFERENCES Diretoria  (id_diretoria),
FOREIGN KEY(id_projeto ) REFERENCES Projeto  (id_projeto)
);

CREATE TABLE Skill (
id_skill SERIAL PRIMARY KEY,
descricao  VARCHAR(255),
nível VARCHAR(255)
);

CREATE TABLE atleta_skill (
id_skill SERIAL,
id_atleta SERIAL,
FOREIGN KEY(id_skill) REFERENCES Skill (id_skill)
);

CREATE TABLE Atleta (
nome VARCHAR(255),
nascimento  TIMESTAMP,
telefone  VARCHAR(255),
convenio VARCHAR(255),
id_atleta SERIAL PRIMARY KEY,
tipo_sangue VARCHAR(255),
cpf VARCHAR(11)
);

CREATE TABLE atleta_posicao (
id_atleta SERIAL,
id_posicao SERIAL,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Posicao (
id_posicao SERIAL PRIMARY KEY,
descricao VARCHAR(255)
);

ALTER TABLE Contato_Emergencia ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE Diretoria  ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_medicamento  ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_alergia ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_fluxocaixa ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE Falta  ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE doenca_atleta ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_evento_posicao ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_evento_posicao ADD FOREIGN KEY(id_posicao) REFERENCES Posicao (id_posicao);
ALTER TABLE atleta_skill ADD FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta);
ALTER TABLE atleta_posicao ADD FOREIGN KEY(id_posicao) REFERENCES Posicao (id_posicao);
