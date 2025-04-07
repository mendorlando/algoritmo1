import heapq
import networkx as nx

class DijkstraInteractivo:
    def __init__(self):
        self.grafo = {}
        self.posiciones = {}
        self.nodo_inicio = None
        self.ultimo_nodo = 0
        
    def agregar_nodo(self, event):
        self.ultimo_nodo += 1
        nuevo_nodo = self.ultimo_nodo
        self.grafo[nuevo_nodo] = {}
        self.posiciones[nuevo_nodo] = (0.5, 0.5)  # Ubicación fija para el ejemplo
        return nuevo_nodo
    
    def ejecutar_dijkstra(self, event):
        if self.nodo_inicio is None:
            return {"error": "Selecciona un nodo inicial primero"}
        
        if len(self.grafo) == 0:
            return {"error": "El grafo está vacío"}
        
        distancias = {nodo: float('infinity') for nodo in self.grafo}
        distancias[self.nodo_inicio] = 0
        padres = {nodo: None for nodo in self.grafo}
        visitados = set()
        
        cola = [(0, self.nodo_inicio)]
        
        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)
            
            if nodo_actual in visitados:
                continue
                
            visitados.add(nodo_actual)
            
            for vecino, peso in self.grafo[nodo_actual].items():
                distancia = distancia_actual + peso
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    padres[vecino] = nodo_actual
                    heapq.heappush(cola, (distancia, vecino))
        
        return distancias
