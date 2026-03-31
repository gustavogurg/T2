"""
   Execution:    python -m algs4.cycle filename.txt
   Data files:   ../dataset/tinyG.txt
                 ../dataset/mediumG.txt
                 ../dataset/largeG.txt
 
   Identifies a cycle.
   Runs in O(E + V) time.
 
  % python -m algs4.cycle ../dataset/tinyG.txt
   3 4 5 3
 
  % python -m algs4.cycle ../dataset/mediumG.txt
   15 0 225 15
 
  % python -m algs4.cycle ../dataset/largeG.txt
   996673 762 840164 4619 785187 194717 996673
 """

from graph import Graph

class Cycle:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        # --- ADICIONADO ---
        self.edge_to = [None for _ in range(G.V)]
        self._cycle = None
        # ------------------
        self._has_cycle = False # Renomeado internamente para não conflitar com o método
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)

    # --- ADICIONADO: Método que a sua Main chama na Questão 4 ---
    def has_cycle(self):
        return self._has_cycle

    # --- ADICIONADO: Método que a sua Main chama na Questão 5 ---
    def cycle(self):
        return self._cycle

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if self._cycle is not None: return
            
            if not self.marked[w]:
                self.edge_to[w] = v # ADICIONADO
                self.dfs(G, w, v)
            elif w != u:
                self._has_cycle = True # ADICIONADO
                # --- ADICIONADO: Reconstrói o caminho do ciclo ---
                self._cycle = []
                x = v
                while x != w:
                    self._cycle.append(x)
                    x = self.edge_to[x]
                self._cycle.append(w)
                self._cycle.append(v)