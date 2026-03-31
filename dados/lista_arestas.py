tabuleiro = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

size = 3

movimentos = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]
#começando por c5 se cavalo em e4

def calc_posicoes(tabuleiro, linha, coluna):
    posicoes = []
    for movimento in movimentos:
        mov_linha = linha + movimento[0]
        mov_coluna = coluna + movimento[1]
        if 0 <= mov_linha < size and 0 <= mov_coluna < size:
            posicoes.append(tabuleiro[mov_linha][mov_coluna])
    return posicoes


lista = []
for i in range(size):
    for j in range(size):
        lista.append(calc_posicoes(tabuleiro, i, j))
        # print(f"Posições para {tabuleiro[i][j]}: {calc_posicoes(tabuleiro, i, j)}")

def exportar_lista():
    arestas = []

    for i in range(size):
        for j in range(size):
            origem = tabuleiro[i][j] - 1
            destinos = calc_posicoes(tabuleiro, i, j)

            for destino in destinos:
                destino -= 1
                if origem < destino:  # evita duplicação
                    arestas.append((origem, destino))

    with open("./grafo.txt", "w") as f:
        f.write(f"{size*size}\n")          # V
        f.write(f"{len(arestas)}\n")      # E
        for v, w in arestas:
            f.write(f"{v} {w}\n")

exportar_lista()