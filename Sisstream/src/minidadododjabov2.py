import random

NUM_DADOS = 40
VALOR_MAXIMO = 999

alvo = int(input("Digite o valor desejado: "))

minimo = NUM_DADOS * 1
maximo = NUM_DADOS * VALOR_MAXIMO

if alvo < minimo or alvo > maximo:
    print(f"\nImpossível!")
    print(f"Com {NUM_DADOS} d999 o valor deve estar entre {minimo} e {maximo}.")
    exit()

dados = []
soma_atual = 0

for i in range(NUM_DADOS):

    dados_restantes = NUM_DADOS - i - 1

    minimo_restante = dados_restantes * 1
    maximo_restante = dados_restantes * VALOR_MAXIMO

    valor_minimo_permitido = max(
        1,
        alvo - soma_atual - maximo_restante
    )

    valor_maximo_permitido = min(
        VALOR_MAXIMO,
        alvo - soma_atual - minimo_restante
    )

    valor = random.randint(
        valor_minimo_permitido,
        valor_maximo_permitido
    )

    dados.append(valor)
    soma_atual += valor

print("\n" + "=" * 60)
print("COMBINAÇÃO ENCONTRADA")
print("=" * 60)

print(f"Alvo: {alvo}")
print(f"Soma obtida: {sum(dados)}")
print(f"Quantidade de dados: {len(dados)}")

print("\nDados:")
print(dados)

print("\nVerificação:")
print(" + ".join(map(str, dados)))
print(f" = {sum(dados)}")