import time
import heapq

def prim_mst(graph: dict, start) -> tuple:
    '''
        Algoritmo de Prim para encontrar a Árvore Geradora Mínima (MST)

        graph: dicionário no formato
               {vertice: [(peso, vizinho), ...]}
        start: vértice inicial

        Retorna:
        mst_edges -> lista de arestas da MST (u, v, peso)
        total_cost -> custo total da MST
        operations -> contador de operações
    '''

    visited = set()
    mst_edges = []
    total_cost = 0
    operations = 0

    # Fila de prioridade (min-heap)
    heap = [(0, start, None)]  # (peso, vertice_atual, vertice_pai)

    while heap and len(visited) < len(graph):
        weight, current, parent = heapq.heappop(heap)
        operations += 1

        if current in visited:
            continue

        visited.add(current)

        if parent is not None:
            mst_edges.append((parent, current, weight))
            total_cost += weight

        for edge_weight, neighbor in graph[current]:
            operations += 1
            if neighbor not in visited:
                heapq.heappush(
                    heap, (edge_weight, neighbor, current)
                )

    return mst_edges, total_cost, operations


# ===============================
# EXEMPLO DE USO
# ===============================

graph = {
    'A': [(1, 'B'), (3, 'C'), (4, 'D')],
    'B': [(1, 'A'), (2, 'D')],
    'C': [(3, 'A'), (5, 'D')],
    'D': [(4, 'A'), (2, 'B'), (5, 'C')]
}

start_vertex = 'A'

print("Resolução do problema da Árvore Geradora Mínima (Prim)\n")

print("Usando o Algoritmo de Prim:")
start_time = time.time()
mst, cost, operations = prim_mst(graph, start_vertex)
end_time = time.time()

print("Grafo de entrada:")
for v in graph:
    print(v, "->", graph[v])

print("\nArestas da Árvore Geradora Mínima:")
for u, v, w in mst:
    print(f"{u} - {v} (peso {w})")

print("\nCusto total da MST:", cost)
print("Operações executadas:", operations)
print(f"Tempo de execução (s): {(end_time - start_time):.8f}")
