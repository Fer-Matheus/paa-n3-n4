import time

def unbounded_knapsack_recursive(values: list, weights: list, capacity: int) -> tuple:
    '''
        Função recursiva para o problema da mochila ilimitada (unbounded knapsack).
        values: lista de valores dos itens
        weights: lista de pesos dos itens
        capacity: capacidade máxima da mochila
        Retorna o valor máximo que pode ser obtido com a capacidade dada.
    '''
    max_values, operations = 0, 0
    for i, value in enumerate(values):
        operations += 1
        if weights[i] <= capacity:
            current_value, operations_rec = unbounded_knapsack_recursive(
                values, weights, capacity - weights[i])
            max_values = max(max_values, value + current_value)
            operations += operations_rec
    return max_values, operations

def memoized_unbounded_knapsack(values: list, weights: list, capacity: int, memo: dict) -> tuple:
    '''
        Função recursiva com memoização para o problema da mochila ilimitada (unbounded knapsack).
        values: lista de valores dos itens
        weights: lista de pesos dos itens
        capacity: capacidade máxima da mochila
        memo: dicionário para armazenar resultados já computados
        Retorna o valor máximo que pode ser obtido com a capacidade dada.
    '''
    max_values, operations = 0, 0
    if capacity in memo:
        return memo[capacity], operations
    
    for i, value in enumerate(values):
        operations += 1
        if weights[i] <= capacity:
            current_value, operations_rec = memoized_unbounded_knapsack(
                values, weights, capacity - weights[i], memo)
            max_values = max(max_values, value + current_value)
            operations += operations_rec

    memo[capacity] = max_values
    return max_values, operations
def unbounded_knapsack_dp(values: list, weights: list, capacity: int) -> tuple:
    '''
        Unbounded Knapsack - Programação Dinâmica (Bottom-Up)

        weights: lista de pesos dos itens
        values: lista de valores dos itens
        capacity: capacidade máxima da mochila

        Retorna:
        dp -> vetor com o valor máximo para cada capacidade
        choice -> vetor para reconstrução da solução
        operations -> contador de operações
    '''
    n = len(weights)
    dp = [0] * (capacity + 1)
    choice = [-1] * (capacity + 1)
    operations = 0

    for w in range(1, capacity + 1):
        for i in range(n):
            operations += 1  
            if weights[i] <= w:
                candidate = dp[w - weights[i]] + values[i]
                if candidate > dp[w]:
                    dp[w] = candidate
                    choice[w] = i

    return dp, choice, operations

# Example usage:
values = [10, 30, 20, 35]
weights = [5, 10, 15, 25]
capacity = 150

print("Resolução do problema da mochila ilimitada (unbounded knapsack)")

print("\nUsando abordagem recursiva simples:")
time_count = time.time()
result, operations = unbounded_knapsack_recursive(values, weights, capacity)
time_count = time.time() - time_count
print(f'Durou: {time_count} segundos')
print(f'Máximo valor do unbounded knapsack = {result}')
print(f'Operações executadas: {operations}')

# Example usage with memoization:
print("\nUsando abordagem recursiva com memoização:")
memo = {}
time_count = time.time()
result_memoized, operations_memoized = memoized_unbounded_knapsack(values, weights, capacity, memo)
time_count = time.time() - time_count
print(f'Durou: {time_count:.8f} segundos com memoização')
print(f'Máximo valor do unbounded knapsack com memoização = {result_memoized}')
print(f'Operações executadas: {operations_memoized}')

# Example usage with dynamic programming:
print("\nUsando abordagem de programação dinâmica:")
start_time = time.time()
dp, choice, operations = unbounded_knapsack_dp(values, weights, capacity)
end_time = time.time()

print("Pesos:", weights)
print("Valores:", values)
print("Capacidade da mochila:", capacity)

print("\nValor máximo obtido:", dp[capacity])

print("\nItens utilizados:")
w = capacity
item_count = {}

while w > 0 and choice[w] != -1:
    i = choice[w]
    item_count[i] = item_count.get(i, 0) + 1
    w -= weights[i]

for i in item_count:
    print(f"Item {i + 1}: {item_count[i]} vez(es)")

print("\nOperações executadas:", operations)
print(f"Tempo de execução (s): {(end_time - start_time):.8f}")
