from graph import Graph

class Cycle:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [None for _ in range(G.V)] # ADICIONADO: "Trilha de migalhas"
        self.cycle_path = None                    # ADICIONADO: Guarda os vértices do ciclo
        self.has_cycle = False
        
        for s in range(G.V):
            # Condição ajustada para parar de buscar se já achou um ciclo
            if not self.marked[s] and self.cycle_path is None: 
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle_path is not None: # Se já achou o ciclo, aborta a busca
                return
            
            if not self.marked[w]:
                self.edge_to[w] = v         # ADICIONADO: Anota de onde veio
                self.dfs(G, w, v)
            elif w != u:
                self.has_cycle = True
                
                # --- ADICIONADO: Constrói a lista do ciclo voltando pelo edge_to ---
                self.cycle_path = []
                x = v
                while x != w:
                    self.cycle_path.append(x)
                    x = self.edge_to[x]
                self.cycle_path.append(w)
                self.cycle_path.append(v)
                self.cycle_path.reverse() # Inverte para mostrar na ordem correta do caminho

    # ADICIONADO: Método para a main pegar o ciclo
    def get_cycle(self):
        return self.cycle_path