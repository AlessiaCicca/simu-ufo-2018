import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getAnni=DAO.getAnni()
        self.grafo = nx.DiGraph()

    def creaGrafo(self, annoStringa):
        anno=int(annoStringa.split("(")[0])
        self.nodi = DAO.getNodi(anno)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(anno)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self,anno):
        self.grafo.clear_edges()
        for nodo1 in self.grafo.nodes:
            for nodo2 in self.grafo.nodes:
                if nodo1!=nodo2 and self.grafo.has_edge(nodo1,nodo2)==False:
                    if DAO.getPeso(nodo1,anno,nodo2)>0:
                     self.grafo.add_edge(nodo1,nodo2)

    def analisi(self, stato):
        prec=[]
        succ=[]
        all=[]
        for nodi in self.grafo.predecessors(stato):
            prec.append(nodi)
        for nodi in self.grafo.successors(stato):
            succ.append(nodi)
        for nodi in nx.dfs_tree(self.grafo,stato):
            all.append(nodi)
        return prec,succ,all

    def getBestPath(self,  nodoIniziale):
        self._soluzione = []
        self._costoMigliore = 0
        parziale = [nodoIniziale]
        self._ricorsione(parziale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale):
        if len(parziale) > self._costoMigliore:
            self._soluzione = copy.deepcopy(parziale)
            self._costoMigliore = len(parziale)

        for n in self.grafo.successors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale)
                parziale.pop()


