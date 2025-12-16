# Prim’s Minimum Spanning Tree (MST)

Implementação do algoritmo de Prim para resolver o problema de otimização da
Árvore Geradora Mínima (Minimum Spanning Tree), cujo objetivo é conectar todos
os vértices de um grafo não direcionado e ponderado com o menor custo total,
sem formar ciclos.

## Algoritmos implementados:
### Algoritmo de Prim (versão gulosa com fila de prioridade)
    - Estratégia: Gulosa (Greedy)
    - Utiliza fila de prioridade (min-heap)
    - Constrói a árvore de forma incremental, escolhendo sempre a aresta de menor peso
      que conecta um vértice já visitado a um vértice não visitado
    - Complexidade: O(E log V)

### Algoritmo de Prim (implementação simples sem heap)
    - Estratégia: Gulosa (Greedy)
    - Utiliza busca linear para selecionar a menor aresta válida
    - Mais simples conceitualmente, porém menos eficiente
    - Complexidade: O(V²)

## Observações
- O algoritmo assume que o grafo é:
  - Não direcionado
  - Conexo
  - Ponderado
- Caso o grafo não seja conexo, o algoritmo gera uma floresta geradora mínima
- O algoritmo de Prim garante solução ótima devido à propriedade do corte

## Aplicações
- Redes de computadores
- Planejamento de redes elétricas
- Otimização de custos em infraestrutura
- Design de circuitos
