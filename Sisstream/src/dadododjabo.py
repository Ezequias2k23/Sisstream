import random
import multiprocessing
import os

DADO_MAX = 999
LIMITE_DADOS = 40

ALVO = int(input("Digite o valor desejado: "))
PROCESSOS = 8


def worker(worker_id, alvo, encontrado):
    falhas = 0

    while not encontrado.is_set():
        total = 0
        rolagens = []

        for _ in range(LIMITE_DADOS):
            dado = random.randint(1, DADO_MAX)

            rolagens.append(dado)
            total += dado

            if dado <= 20:
                break

        falhas += 1

        print(
            f"[Worker {worker_id}] "
            f"Falha #{falhas} | "
            f"Total={total} | "
            f"Dados={len(rolagens)} | "
            f"Rolagens={rolagens}",
            flush=True
        )

        if total == alvo:
            encontrado.set()

            print("\n" + "=" * 70)
            print("RESULTADO ENCONTRADO")
            print("=" * 70)
            print(f"Worker: {worker_id}")
            print(f"Falhas até encontrar: {falhas}")
            print(f"Valor encontrado: {total}")
            print(f"Quantidade de dados: {len(rolagens)}")
            print(f"Rolagens finais: {rolagens}")
            print("=" * 70)


if __name__ == "__main__":
    encontrado = multiprocessing.Event()

    processos = []

    for i in range(PROCESSOS):
        p = multiprocessing.Process(
            target=worker,
            args=(i + 1, ALVO, encontrado)
        )

        p.start()
        processos.append(p)

    for p in processos:
        p.join()