-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Medicamento  (
id_medicamento  INTEGER PRIMARY KEY,
dose VARCHAR(50),
nome VARCHAR(50)
);

CREATE TABLE Efeito_Colateral  (
id_efeito_colateral INTEGER PRIMARY KEY,
descricao VARCHAR(300)
);

CREATE TABLE Doenca  (
descricao VARCHAR(300),
id_doenca  INTEGER PRIMARY KEY
);

CREATE TABLE Atleta (
nome VARCHAR(50),
nascimento  TIMESTAMP,
telefone  VARCHAR(50),
convenio VARCHAR(50),
id_atleta INTEGER PRIMARY KEY,
tipo_sangue VARCHAR(3),
cpf VARCHAR(50)
);

CREATE TABLE Alergia  (
id_alergia  INTEGER PRIMARY KEY,
descricao  VARCHAR(50)
);

CREATE TABLE Diretoria  (
descricao VARCHAR(50),
id_diretoria  INTEGER PRIMARY KEY,
id_atleta INTEGER,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Projeto  (
id_projeto  INTEGER PRIMARY KEY,
data TIMESTAMP,
descricao  VARCHAR(50)
);

CREATE TABLE Contato_Emergencia (
telefone  VARCHAR(50),
nome VARCHAR(50),
id_contato_emergencia  INTEGER PRIMARY KEY,
id_atleta INTEGER,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Skill (
id_skill INTEGER PRIMARY KEY,
nivel INTEGER,
descricao  VARCHAR(50)
);

CREATE TABLE Evento  (
id_evento  INTEGER PRIMARY KEY,
local  VARCHAR(50),
data TIMESTAMP,
descricao  VARCHAR(50)
);

CREATE TABLE Falta  (
id_falta  INTEGER PRIMARY KEY,
data TIMESTAMP,
descricao  VARCHAR(50),
id_atleta INTEGER,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Fluxo_Caixa (
id_fluxo_caixa INTEGER PRIMARY KEY,
valor  DECIMAL(10),
data TIMESTAMP,
flag_entrada_saida INTEGER,
descricao  VARCHAR(50)
);

CREATE TABLE atleta_fluxo_caixa (
id_atleta INTEGER,
id_fluxo_caixa INTEGER,
PRIMARY KEY(id_atleta,id_fluxo_caixa),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_fluxo_caixa) REFERENCES Fluxo_Caixa (id_fluxo_caixa)
);

CREATE TABLE medicamento_efeito_colateral (
id_medicamento  INTEGER,
id_efeito_colateral INTEGER,
PRIMARY KEY(id_medicamento ,id_efeito_colateral),
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento),
FOREIGN KEY(id_efeito_colateral) REFERENCES Efeito_Colateral  (id_efeito_colateral)
);

CREATE TABLE atleta_medicamento  (
id_atleta INTEGER,
id_medicamento  INTEGER,
PRIMARY KEY(id_atleta,id_medicamento),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento)
);

CREATE TABLE atleta_alergia (
id_atleta INTEGER,
id_alergia  INTEGER,
PRIMARY KEY(id_atleta,id_alergia),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_alergia ) REFERENCES Alergia  (id_alergia)
);

CREATE TABLE diretoria_projeto (
id_diretoria  INTEGER,
id_projeto  INTEGER,
PRIMARY KEY(id_diretoria ,id_projeto),
FOREIGN KEY(id_diretoria ) REFERENCES Diretoria  (id_diretoria),
FOREIGN KEY(id_projeto ) REFERENCES Projeto  (id_projeto)
);

CREATE TABLE evento_fluxo_caixa (
id_fluxo_caixa INTEGER,
id_evento  INTEGER,
PRIMARY KEY(id_fluxo_caixa,id_evento),
FOREIGN KEY(id_fluxo_caixa) REFERENCES Fluxo_Caixa (id_fluxo_caixa),
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE atleta_posicao (
id_posicao INTEGER,
id_atleta INTEGER,
PRIMARY KEY(id_posicao,id_atleta),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE atleta_skill (
id_skill INTEGER,
id_atleta INTEGER,
PRIMARY KEY(id_skill,id_atleta),
FOREIGN KEY(id_skill) REFERENCES Skill (id_skill),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Posicao (
id_posicao INTEGER PRIMARY KEY,
descricao VARCHAR(50)
);

CREATE TABLE atleta_evento_posicao (
id_evento  INTEGER,
id_atleta INTEGER,
id_posicao INTEGER,
PRIMARY KEY(id_evento ,id_atleta,id_posicao)
);

CREATE TABLE doenca_atleta (
id_atleta INTEGER,
id_doenca  INTEGER,
PRIMARY KEY(id_atleta,id_doenca),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_doenca ) REFERENCES Doenca  (id_doenca)
);

ALTER TABLE atleta_posicao ADD FOREIGN KEY(id_posicao) REFERENCES Posicao (id_posicao);
