-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Medicamento  (
id_medicamento  INTEGER PRIMARY KEY NOT NULL,
dose VARCHAR(50) NOT NULL,
nome VARCHAR(50) NOT NULL
);

CREATE TABLE Efeito_Colateral  (
id_efeito_colateral INTEGER PRIMARY KEY NOT NULL,
descricao VARCHAR(300) NOT NULL
);

CREATE TABLE Doenca  (
descricao VARCHAR(300) NOT NULL,
id_doenca  INTEGER PRIMARY KEY NOT NULL
);

CREATE TABLE Atleta (
nome VARCHAR(50) NOT NULL,
nascimento  TIMESTAMP NOT NULL,
telefone  VARCHAR(50) NOT NULL,
convenio VARCHAR(50) NOT NULL,
id_atleta INTEGER PRIMARY KEY NOT NULL,
tipo_sangue VARCHAR(3) NOT NULL,
cpf VARCHAR(50) NOT NULL
);

CREATE TABLE Alergia  (
id_alergia  INTEGER PRIMARY KEY NOT NULL,
descricao  VARCHAR(50) NOT NULL
);

CREATE TABLE Diretoria  (
descricao VARCHAR(50) NOT NULL,
id_diretoria  INTEGER PRIMARY KEY NOT NULL,
id_atleta INTEGER NOT NULL,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Projeto  (
id_projeto  INTEGER PRIMARY KEY NOT NULL,
data TIMESTAMP NOT NULL,
descricao  VARCHAR(50) NOT NULL
);

CREATE TABLE Contato_Emergencia (
telefone  VARCHAR(50) NOT NULL,
nome VARCHAR(50) NOT NULL,
id_contato_emergencia  INTEGER PRIMARY KEY NOT NULL,
id_atleta INTEGER NOT NULL,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Skill (
id_skill INTEGER PRIMARY KEY NOT NULL,
nivel INTEGER NOT NULL,
descricao  VARCHAR(50) NOT NULL
);

CREATE TABLE Evento  (
id_evento  INTEGER PRIMARY KEY NOT NULL,
local  VARCHAR(50) NOT NULL,
data TIMESTAMP NOT NULL,
descricao  VARCHAR(50) NOT NULL
);

CREATE TABLE Falta  (
id_falta  INTEGER PRIMARY KEY NOT NULL,
data TIMESTAMP NOT NULL,
descricao  VARCHAR(50) NOT NULL,
id_atleta INTEGER NOT NULL,
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Fluxo_Caixa (
id_fluxo_caixa INTEGER PRIMARY KEY NOT NULL,
valor  DECIMAL(10) NOT NULL,
data TIMESTAMP NOT NULL,
flag_entrada_saida INTEGER NOT NULL,
descricao  VARCHAR(50) NOT NULL
);

CREATE TABLE atleta_fluxo_caixa (
id_atleta INTEGER NOT NULL,
id_fluxo_caixa INTEGER NOT NULL,
PRIMARY KEY(id_atleta,id_fluxo_caixa),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_fluxo_caixa) REFERENCES Fluxo_Caixa (id_fluxo_caixa)
);

CREATE TABLE medicamento_efeito_colateral (
id_medicamento  INTEGER NOT NULL,
id_efeito_colateral INTEGER NOT NULL,
PRIMARY KEY(id_medicamento ,id_efeito_colateral),
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento),
FOREIGN KEY(id_efeito_colateral) REFERENCES Efeito_Colateral  (id_efeito_colateral)
);

CREATE TABLE atleta_medicamento  (
id_atleta INTEGER NOT NULL,
id_medicamento  INTEGER NOT NULL,
PRIMARY KEY(id_atleta,id_medicamento),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_medicamento ) REFERENCES Medicamento  (id_medicamento)
);

CREATE TABLE atleta_alergia (
id_atleta INTEGER NOT NULL,
id_alergia  INTEGER NOT NULL,
PRIMARY KEY(id_atleta,id_alergia),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_alergia ) REFERENCES Alergia  (id_alergia)
);

CREATE TABLE diretoria_projeto (
id_diretoria  INTEGER NOT NULL,
id_projeto  INTEGER NOT NULL,
PRIMARY KEY(id_diretoria ,id_projeto),
FOREIGN KEY(id_diretoria ) REFERENCES Diretoria  (id_diretoria),
FOREIGN KEY(id_projeto ) REFERENCES Projeto  (id_projeto)
);

CREATE TABLE evento_fluxo_caixa (
id_fluxo_caixa INTEGER NOT NULL,
id_evento  INTEGER NOT NULL,
PRIMARY KEY(id_fluxo_caixa,id_evento),
FOREIGN KEY(id_fluxo_caixa) REFERENCES Fluxo_Caixa (id_fluxo_caixa),
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento)
);

CREATE TABLE atleta_posicao (
id_posicao INTEGER NOT NULL,
id_atleta INTEGER NOT NULL,
PRIMARY KEY(id_posicao,id_atleta),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE atleta_skill (
id_skill INTEGER NOT NULL,
id_atleta INTEGER NOT NULL,
PRIMARY KEY(id_skill,id_atleta),
FOREIGN KEY(id_skill) REFERENCES Skill (id_skill),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta)
);

CREATE TABLE Posicao (
id_posicao INTEGER PRIMARY KEY NOT NULL,
descricao VARCHAR(50) NOT NULL
);

CREATE TABLE atleta_evento_posicao (
id_evento  INTEGER NOT NULL,
id_atleta INTEGER NOT NULL,
id_posicao INTEGER NOT NULL,
PRIMARY KEY(id_evento ,id_atleta,id_posicao),
FOREIGN KEY(id_evento ) REFERENCES Evento  (id_evento),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_posicao) REFERENCES Posicao (id_posicao)
);

CREATE TABLE doenca_atleta (
id_atleta INTEGER NOT NULL,
id_doenca  INTEGER NOT NULL,
PRIMARY KEY(id_atleta,id_doenca),
FOREIGN KEY(id_atleta) REFERENCES Atleta (id_atleta),
FOREIGN KEY(id_doenca ) REFERENCES Doenca  (id_doenca)
);

ALTER TABLE atleta_posicao ADD FOREIGN KEY(id_posicao) REFERENCES Posicao (id_posicao);