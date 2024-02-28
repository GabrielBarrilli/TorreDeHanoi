def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

def main():
    print("Bem-vindo ao jogo da Torre de Hanoi!")
    num_pecas = int(input("Digite o número de peças: "))
    torre_origem = input("Digite a torre de origem (A, B, C): ").upper()
    torre_destino = input("Digite a torre de destino (A, B, C): ").upper()
    torre_auxiliar = input("Digite a torre auxiliar (A, B, C): ").upper()

    print(f"\nSolução para a Torre de Hanoi com {num_pecas} peças:")
    torre_hanoi(num_pecas, torre_origem, torre_destino, torre_auxiliar)

if __name__ == "__main__":
    main()
