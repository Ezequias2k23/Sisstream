from conexao import conectar

class ProducaoDAO:
    def inserir(self, titulo, descricao, ano_lancamento, classificacao_indicativa, tipo):
        sql = """
            INSERT INTO producao (titulo, descricao, ano_lancamento, classificacao_indicativa, tipo)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_producao;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (titulo, descricao, ano_lancamento, classificacao_indicativa, tipo))
                    return cur.fetchone()[0]
        finally:
            conn.close()

    def listar(self):
        sql = """
            SELECT id_producao, titulo, ano_lancamento, classificacao_indicativa, tipo
            FROM producao
            ORDER BY id_producao;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        finally:
            conn.close()

    def atualizar(self, id_producao, titulo, descricao, ano_lancamento, classificacao_indicativa, tipo):
        sql = """
            UPDATE producao
            SET titulo=%s, descricao=%s, ano_lancamento=%s, classificacao_indicativa=%s, tipo=%s
            WHERE id_producao=%s;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (titulo, descricao, ano_lancamento, classificacao_indicativa, tipo, id_producao))
                    return cur.rowcount
        finally:
            conn.close()

    def deletar(self, id_producao):
        sql = "DELETE FROM producao WHERE id_producao=%s;"
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id_producao,))
                    return cur.rowcount
        finally:
            conn.close()