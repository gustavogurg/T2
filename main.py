from lista_adj import retornar_lista
from algs4.graph import Graph
from algs4.cc import CC  
from algs4.cycle import Cycle
from algs4.breadth_first_paths import BreadthFirstPaths
import networkx as nx

# Perguntas que o programa deve responder

#     Qual é o grafo do cavalo informado, na forma de lista de adjacência?
#     Quais são as componentes conexas do grafo?
#     Qual é a distância mínima entre as posições (0,0) e (2,2) da matriz do tabuleiro, considerando os movimentos válidos do cavalo?
#     O grafo possui ciclo? Apresente também a análise de complexidade de tempo e de espaço do algoritmo utilizado.
#     Se o grafo possuir ciclo, quais são os vértices de um ciclo encontrado?


lista, size = retornar_lista()

Grafo = Graph(size**2)
for i in range(len(lista)):
    for pos in lista[i]:
        Grafo.add_edge(i, (pos)-1)

#printar lista de adjacências
print("Lista de adjacências:")
for v in range(int(Grafo.V)):
    print(f"{v}:", end=" ")
    for w in Grafo.adj[v]:
        print(w, end=" ")
    print()


#Componentes conexos
cc = CC(Grafo)
print("Número de componentes conexos: " + str((cc.count)))
print("Componentes conexos:")

for v in range(Grafo.V):
    print(f"Vértice {v} -> componente {cc.id[v]}")

# calculkar distancia entre (0,0) e (2,2)
def calcular_distancia(grafo, origem, destino):
    bfs = BreadthFirstPaths(grafo, origem)
    if not bfs.has_path_to(destino):
        return -1
    caminho = list(bfs.path_to(destino))
    # print(caminho)
    return len(caminho) - 1

distancia = calcular_distancia(Grafo, 0, 8)
print("A distância entre (0,0) e (2,2) é: " + str(distancia))

cycle = Cycle(Grafo)

#Algoritmo de Johson

def algs4_to_nx_digraph(G_algs4):
    G_nx = nx.DiGraph()
    
    for v in range(G_algs4.V):
        for w in G_algs4.adj[v]:
            G_nx.add_edge(v, w)
    
    return G_nx

G_nx = algs4_to_nx_digraph(Grafo)

lista_ciclo = list(nx.simple_cycles(G_nx))

if cycle.has_cycle == True:
    print("O grafo possui ciclo.")
    print("Os ciclos encontrados são: " )
    for ciclo in lista_ciclo:
        if len(ciclo) > 3:  # filtra size
            print(ciclo)
else:    
    print("O grafo não possui ciclo.") 



