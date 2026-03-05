from conexao import conectar

class AvaliacaoDAO:
    def inserir(self, nota, comentario, id_usuario, id_producao):
        sql = """
            INSERT INTO avaliacao (nota, comentario, data_avaliacao, id_usuario, id_producao)
            VALUES (%s, %s, NOW(), %s, %s)
            RETURNING id_avaliacao;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (nota, comentario, id_usuario, id_producao))
                    return cur.fetchone()[0]
        finally:
            conn.close()

    def listar(self):
        sql = """
            SELECT id_avaliacao, nota, comentario, data_avaliacao, id_usuario, id_producao
            FROM avaliacao
            ORDER BY id_avaliacao;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        finally:
            conn.close()

    def atualizar(self, id_avaliacao, nota, comentario):
        sql = """
            UPDATE avaliacao
            SET nota=%s, comentario=%s
            WHERE id_avaliacao=%s;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (nota, comentario, id_avaliacao))
                    return cur.rowcount
        finally:
            conn.close()

    def deletar(self, id_avaliacao):
        sql = "DELETE FROM avaliacao WHERE id_avaliacao=%s;"
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id_avaliacao,))
                    return cur.rowcount
        finally:
            conn.close()

    # JOIN + GROUP BY
    def media_por_producao(self):
        sql = """
            SELECT p.id_producao, p.titulo, ROUND(AVG(a.nota), 2) AS media
            FROM avaliacao a
            JOIN producao p ON p.id_producao = a.id_producao
            GROUP BY p.id_producao, p.titulo
            ORDER BY media DESC;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        finally:
            conn.close()

    # Avaliações detalhadas (JOIN 3 tabelas)
    def listar_avaliacoes_detalhadas(self):
        sql = """
            SELECT
                a.id_avaliacao,
                u.nome AS usuario,
                p.titulo AS producao,
                a.nota,
                a.comentario,
                a.data_avaliacao
            FROM avaliacao a
            JOIN usuario u ON u.id_usuario = a.id_usuario
            JOIN producao p ON p.id_producao = a.id_producao
            ORDER BY a.data_avaliacao DESC, a.id_avaliacao DESC;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        finally:
            conn.close()