CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_nascimento DATE,
    pais VARCHAR(50),
    data_criacao_conta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE producao (
    id_producao SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    descricao TEXT,
    ano_lancamento INT,
    classificacao_indicativa VARCHAR(10),
    tipo VARCHAR(10)
);

CREATE TABLE avaliacao (
    id_avaliacao SERIAL PRIMARY KEY,
    nota DECIMAL(3,2),
    comentario TEXT,
    data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    id_producao INT REFERENCES producao(id_producao) ON DELETE CASCADE
);