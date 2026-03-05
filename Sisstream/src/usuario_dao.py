from conexao import conectar

class UsuarioDAO:
    def inserir(self, nome, email, data_nascimento, pais):
        sql = """
            INSERT INTO usuario (nome, email, data_nascimento, pais, data_criacao_conta)
            VALUES (%s, %s, %s, %s, NOW())
            RETURNING id_usuario;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (nome, email, data_nascimento, pais))
                    return cur.fetchone()[0]
        finally:
            conn.close()

    def listar(self):
        sql = """
            SELECT id_usuario, nome, email, data_nascimento, pais, data_criacao_conta
            FROM usuario
            ORDER BY id_usuario;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        finally:
            conn.close()

    def atualizar(self, id_usuario, nome, email, data_nascimento, pais):
        sql = """
            UPDATE usuario
            SET nome=%s, email=%s, data_nascimento=%s, pais=%s
            WHERE id_usuario=%s;
        """
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (nome, email, data_nascimento, pais, id_usuario))
                    return cur.rowcount
        finally:
            conn.close()

    def deletar(self, id_usuario):
        sql = "DELETE FROM usuario WHERE id_usuario=%s;"
        conn = conectar()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id_usuario,))
                    return cur.rowcount
        finally:
            conn.close()