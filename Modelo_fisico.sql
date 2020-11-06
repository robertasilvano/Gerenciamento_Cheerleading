-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.

CREATE TABLE Contato_Emergencia (
telefone  VARCHAR(255),
id_emergencia  INTEGER PRIMARY KEY,
nome VARCHAR(255),
id_atleta INTEGER
);

CREATE TABLE Doenca  (
descricao VARCHAR(255),
id_doenca  INTEGER PRIMARY KEY
);

CREATE TABLE Medicamento  (
id_medicamento  INTEGER PRIMARY KEY,
nome VARCHAR(255),
dose VARCHAR(255)
);

CREATE TABLE Efeito_Colateral  (
id_efeito INTEGER PRIMARY KEY,
descricao VARCHAR(255)
);

CREATE TABLE Projeto  (
id_projeto  INTEGER PRIMARY KEY,
descricao  VARCHAR(255),
data TIMESTAMP
);

CREATE TABLE Alergia  (
descricao  VARCHAR(255),
id_alergia  INTEGER PRIMARY KEY
);

CREATE TABLE Diretoria  (
id_diretoria  INTEGER PRIMARY KEY,
cargo  VARCHAR(255),
id_atleta INTEGER
);

CREATE TABLE atleta_medicamento  (
id_atleta INTEGER,
id_medicamento  INTEGER,
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento)
);

CREATE TABLE medicamento_efeitocolateral (
id_medicamento  INTEGER,
id_efeito INTEGER,
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento),
FOREIGN KEY(id_efeito) REFERENCES Efeito_Colateral  (id_efeito)
);

CREATE TABLE atleta_alergia (
id_atleta INTEGER,
id_alergia  INTEGER,
FOREIGN KEY(id_alergia ) REFERENCES Alergia  (id_alergia)
);

CREATE TABLE Evento  (
local  VARCHAR(255),
id_evento  INTEGER PRIMARY KEY,
data TIMESTAMP,
descricao  VARCHAR(255)
);

CREATE TABLE Fluxo_Caixa (
id_fluxo  INTEGER PRIMARY KEY,
descricao  VARCHAR(255),
valor  NUMERIC(10),
flag_entrada_saida NUMERIC(10),
data TIMESTAMP
);

CREATE TABLE evento_fluxocaixa (
id_fluxo  INTEGER,
id_evento  INTEGER,
FOREIGN KEY(id_fluxo ) REFERENCES Fluxo_Caixa (id_fluxo),
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE atleta_fluxocaixa (
id_atleta INTEGER,
id_fluxo  INTEGER,
FOREIGN KEY(id_fluxo ) REFERENCES Fluxo_Caixa (id_fluxo)
);

CREATE TABLE Falta  (
id_falta  INTEGER PRIMARY KEY,
descricao  VARCHAR(255),
data TIMESTAMP,
id_atleta INTEGER
);

CREATE TABLE doenca_atleta (
id_atleta INTEGER,
id_doenca  INTEGER,
FOREIGN KEY(id_doenca ) REFERENCES Doenca  (id_doenca)
);

CREATE TABLE atleta_evento_posicao (
id_atleta INTEGER,
id_evento  INTEGER,
id_posicao INTEGER,
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE diretoria_projeto (
id_diretoria  INTEGER,
id_projeto  INTEGER,
FOREIGN KEY(id_diretoria ) REFERENCES Diretoria  (id_diretoria),
FOREIGN KEY(id_projeto ) REFERENCES Projeto  (id_projeto)
);

CREATE TABLE Skill (
id_skill INTEGER PRIMARY KEY,
descricao  VARCHAR(255),
nível VARCHAR(255)
);

CREATE TABLE atleta_skill (
id_skill INTEGER,
id_atleta INTEGER,
FOREIGN KEY(id_skill) REFERENCES Skill (id_skill)
);

CREATE TABLE Atleta (
nome VARCHAR(255),
nascimento  TIMESTAMP,
telefone  VARCHAR(255),
convenio VARCHAR(255),
id_atleta INTEGER PRIMARY KEY,
tipo_sangue VARCHAR(255),
cpf VARCHAR(11)
);

CREATE TABLE atleta_posicao (
id_atleta INTEGER,
id_posicao INTEGER,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Posicao (
id_posicao INTEGER PRIMARY KEY,
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
