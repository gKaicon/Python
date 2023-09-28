def imprimir_jogo(jogo):
    print("\n\n\t 0   1   2\n\n")
    for l in range(3):
        for c in range(3):
            if c == 0:
                print("\t", end="")
            print(f" {jogo[l][c]} ", end="")
            if c < 2:
                print("|", end="")
            if c == 2:
                print(f"  {l}", end="")
        if l < 2:
            print("\n\t-----------")
        print("")

def verificar_ganhador(jogo):
    for l in range(3):
        # Verificar linhas
        if jogo[l][0] == jogo[l][1] == jogo[l][2] and jogo[l][0] != ' ':
            return jogo[l][0]
        # Verificar colunas
        if jogo[0][l] == jogo[1][l] == jogo[2][l] and jogo[0][l] != ' ':
            return jogo[0][l]
    # Verificar diagonais
    if jogo[0][0] == jogo[1][1] == jogo[2][2] and jogo[0][0] != ' ':
        return jogo[0][0]
    if jogo[0][2] == jogo[1][1] == jogo[2][0] and jogo[0][2] != ' ':
        return jogo[0][2]
    return None

def jogar_jogo_da_velha():
    opcao = 1
    while opcao == 1:
        jogador = '0'; ganhou = None; jogadas = 0; jogo = [[' ' for _ in range(3)] for _ in range(3)]
        while ganhou is None and jogadas < 9:
            imprimir_jogo(jogo)
            print("\nJOGADOR 1 = 0\nJOGADOR 2 = X\n"f"JOGADOR {jogador}: Digite a linha e a coluna que deseja jogar: ")
            linha, coluna = map(int, input().split())
            if 0 <= linha < 3 and 0 <= coluna < 3 and jogo[linha][coluna] == ' ':
                jogo[linha][coluna] = jogador
                jogador = 'X' if jogador == '0' else '0'
                jogadas += 1
            else:
                print("Jogada inválida. Tente novamente.")
            ganhador = verificar_ganhador(jogo)
            if ganhador:
                imprimir_jogo(jogo)
                print(f"\nParabéns! O jogador {ganhador} venceu!\n")
                ganhou = ganhador
        if ganhou is None:
            imprimir_jogo(jogo)
            print("\nO jogo terminou em empate!\n")
        print("Digite 1 para jogar novamente ou qualquer outra tecla para sair:")
        opcao = int(input())
if __name__ == "__main__":
    jogar_jogo_da_velha()