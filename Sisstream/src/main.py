from decimal import Decimal, InvalidOperation, ROUND_DOWN

from usuario_dao import UsuarioDAO
from producao_dao import ProducaoDAO
from avaliacao_dao import AvaliacaoDAO


def ler_nota_1_a_5():
    """
    - Aceita nota apenas de 1 a 5 (inclusive)
    - Aceita decimal: 3.5, 3.75, etc.
    - CORTA para 2 casas (sem arredondar): 3.1778 -> 3.17
    - Rejeita valores fora do intervalo (ex: 55, 0.5, 6)
    """
    while True:
        texto = input("Nota (1 a 5, pode ser decimal): ").strip().replace(",", ".")

        if texto == "":
            print("Erro: a nota só pode ir de 1 a 5 (com variações decimais).")
            continue

        try:
            valor = Decimal(texto)
        except InvalidOperation:
            print("Erro: nota inválida. Use números entre 1 e 5 (ex: 4, 3.5, 2.75).")
            continue

        # Corta para 2 casas, sem arredondar
        valor = valor.quantize(Decimal("0.00"), rounding=ROUND_DOWN)

        if valor < Decimal("1.00") or valor > Decimal("5.00"):
            print("Erro: a nota só pode ir de 1 a 5 (com variações decimais).")
            continue

        return valor


usuario_dao = UsuarioDAO()
producao_dao = ProducaoDAO()
avaliacao_dao = AvaliacaoDAO()

while True:
    print("Menu Principal")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Inserir produção")
    print("4 - Listar produções")
    print("5 - Criar avaliação")
    print("6 - Média das produções")
    print("7 - Ver todas as avaliações")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        data = input("Data nascimento (YYYY-MM-DD): ")
        pais = input("País: ")

        id_usuario = usuario_dao.inserir(nome, email, data, pais)
        print("Usuário criado com ID:", id_usuario)

    elif opcao == "2":
        usuarios = usuario_dao.listar()
        print("\nLista de usuários:")
        for u in usuarios:
            print(u)

    elif opcao == "3":
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        ano = int(input("Ano lançamento: "))
        classificacao = input("Classificação indicativa: ")
        tipo = input("Tipo (FILME/SERIE): ")

        id_producao = producao_dao.inserir(titulo, descricao, ano, classificacao, tipo)
        print("Produção criada com ID:", id_producao)

    elif opcao == "4":
        producoes = producao_dao.listar()
        print("\nLista de produções:")
        for p in producoes:
            print(p)

    elif opcao == "5":
        nota = ler_nota_1_a_5()
        comentario = input("Comentário: ")
        id_usuario = int(input("ID do usuário: "))
        id_producao = int(input("ID da produção: "))

        id_avaliacao = avaliacao_dao.inserir(nota, comentario, id_usuario, id_producao)
        print("Avaliação criada com ID:", id_avaliacao)

    elif opcao == "6":
        print("Medias das Produções")
        medias = avaliacao_dao.media_por_producao()
        for m in medias:
            print(m)

    elif opcao == "7":
        print("Todas as avaliações")
        avals = avaliacao_dao.listar_avaliacoes_detalhadas()
        for a in avals:
            print(a)

    elif opcao == "8":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")