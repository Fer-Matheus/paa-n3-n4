import time
import matplotlib.pyplot as plt
import numpy as np
from unbounded_knapsack_recursive import (
    unbounded_knapsack_recursive,
    memoized_unbounded_knapsack,
    unbounded_knapsack_dp
)

def run_benchmarks():
    """
    Executa benchmarks dos três algoritmos com diferentes tamanhos de entrada
    e coleta métricas de tempo de execução e número de operações
    """
    # Dados fixos para os itens
    values = [10, 30, 20, 35]
    weights = [5, 10, 15, 25]
    
    # Diferentes capacidades para testar (aumentando progressivamente)
    capacities = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Dicionários para armazenar resultados
    results = {
        'recursive': {'times': [], 'operations': [], 'values': []},
        'memoized': {'times': [], 'operations': [], 'values': []},
        'dynamic': {'times': [], 'operations': [], 'values': []}
    }
    
    print("="*70)
    print("BENCHMARK: Unbounded Knapsack - Comparação de Algoritmos")
    print("="*70)
    print(f"Valores dos itens: {values}")
    print(f"Pesos dos itens: {weights}")
    print("="*70)
    
    for capacity in capacities:
        print(f"\n{'='*70}")
        print(f"Testando com capacidade: {capacity}")
        print(f"{'='*70}")
        
        # 1. Algoritmo Recursivo Simples
        print("\n1. Recursivo Simples:")
        try:
            start_time = time.time()
            result, operations = unbounded_knapsack_recursive(values, weights, capacity)
            execution_time = time.time() - start_time
            
            results['recursive']['times'].append(execution_time)
            results['recursive']['operations'].append(operations)
            results['recursive']['values'].append(result)
            
            print(f"   Valor máximo: {result}")
            print(f"   Tempo: {execution_time:.6f}s")
            print(f"   Operações: {operations}")
        except RecursionError:
            print("   ⚠️ Recursão muito profunda (capacidade muito grande)")
            results['recursive']['times'].append(None)
            results['recursive']['operations'].append(None)
            results['recursive']['values'].append(None)
        
        # 2. Algoritmo Recursivo com Memoização
        print("\n2. Recursivo com Memoização:")
        memo = {}
        start_time = time.time()
        result_memo, operations_memo = memoized_unbounded_knapsack(
            values, weights, capacity, memo
        )
        execution_time_memo = time.time() - start_time
        
        results['memoized']['times'].append(execution_time_memo)
        results['memoized']['operations'].append(operations_memo)
        results['memoized']['values'].append(result_memo)
        
        print(f"   Valor máximo: {result_memo}")
        print(f"   Tempo: {execution_time_memo:.6f}s")
        print(f"   Operações: {operations_memo}")
        
        # 3. Programação Dinâmica (Bottom-Up)
        print("\n3. Programação Dinâmica (Bottom-Up):")
        start_time = time.time()
        dp, choice, operations_dp = unbounded_knapsack_dp(values, weights, capacity)
        execution_time_dp = time.time() - start_time
        
        results['dynamic']['times'].append(execution_time_dp)
        results['dynamic']['operations'].append(operations_dp)
        results['dynamic']['values'].append(dp[capacity])
        
        print(f"   Valor máximo: {dp[capacity]}")
        print(f"   Tempo: {execution_time_dp:.6f}s")
        print(f"   Operações: {operations_dp}")
    
    return capacities, results


def generate_graphs(capacities, results):
    """
    Gera gráficos comparativos dos algoritmos
    """
    # Filtra valores None (casos onde recursivo falhou)
    cap_recursive = []
    times_recursive = []
    ops_recursive = []
    
    for i, (t, o) in enumerate(zip(
        results['recursive']['times'], 
        results['recursive']['operations']
    )):
        if t is not None and o is not None:
            cap_recursive.append(capacities[i])
            times_recursive.append(t)
            ops_recursive.append(o)
    
    # Configuração do estilo
    plt.style.use('seaborn-v0_8-darkgrid')
    fig = plt.figure(figsize=(16, 10))
    
    # 1. Comparação de Tempo de Execução
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(cap_recursive, times_recursive, 'o-', label='Recursivo Simples', 
             linewidth=2, markersize=8, color='#e74c3c')
    ax1.plot(capacities, results['memoized']['times'], 's-', 
             label='Recursivo + Memoização', linewidth=2, markersize=8, color='#3498db')
    ax1.plot(capacities, results['dynamic']['times'], '^-', 
             label='Programação Dinâmica', linewidth=2, markersize=8, color='#2ecc71')
    ax1.set_xlabel('Capacidade da Mochila', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Tempo de Execução (segundos)', fontsize=12, fontweight='bold')
    ax1.set_title('Comparação de Tempo de Execução', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # 2. Comparação de Número de Operações
    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(cap_recursive, ops_recursive, 'o-', label='Recursivo Simples', 
             linewidth=2, markersize=8, color='#e74c3c')
    ax2.plot(capacities, results['memoized']['operations'], 's-', 
             label='Recursivo + Memoização', linewidth=2, markersize=8, color='#3498db')
    ax2.plot(capacities, results['dynamic']['operations'], '^-', 
             label='Programação Dinâmica', linewidth=2, markersize=8, color='#2ecc71')
    ax2.set_xlabel('Capacidade da Mochila', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Número de Operações', fontsize=12, fontweight='bold')
    ax2.set_title('Comparação de Número de Operações', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    # 3. Tempo de Execução (escala logarítmica)
    ax3 = plt.subplot(2, 2, 3)
    ax3.semilogy(cap_recursive, times_recursive, 'o-', label='Recursivo Simples', 
                 linewidth=2, markersize=8, color='#e74c3c')
    ax3.semilogy(capacities, results['memoized']['times'], 's-', 
                 label='Recursivo + Memoização', linewidth=2, markersize=8, color='#3498db')
    ax3.semilogy(capacities, results['dynamic']['times'], '^-', 
                 label='Programação Dinâmica', linewidth=2, markersize=8, color='#2ecc71')
    ax3.set_xlabel('Capacidade da Mochila', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Tempo de Execução (log scale)', fontsize=12, fontweight='bold')
    ax3.set_title('Tempo de Execução (Escala Logarítmica)', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3, which='both')
    
    # 4. Comparação de Eficiência (Operações vs Tempo)
    ax4 = plt.subplot(2, 2, 4)
    if ops_recursive and times_recursive:
        ax4.scatter(ops_recursive, times_recursive, s=100, alpha=0.6, 
                   label='Recursivo Simples', color='#e74c3c')
    ax4.scatter(results['memoized']['operations'], results['memoized']['times'], 
               s=100, alpha=0.6, label='Recursivo + Memoização', color='#3498db')
    ax4.scatter(results['dynamic']['operations'], results['dynamic']['times'], 
               s=100, alpha=0.6, label='Programação Dinâmica', color='#2ecc71')
    ax4.set_xlabel('Número de Operações', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Tempo de Execução (segundos)', fontsize=12, fontweight='bold')
    ax4.set_title('Eficiência: Operações vs Tempo', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('unbounded_knapsack_comparison.png', dpi=300, bbox_inches='tight')
    print("\n✅ Gráfico salvo como 'unbounded_knapsack_comparison.png'")
    
    # Gráfico adicional: Barras comparativas para capacidade específica
    fig2, (ax5, ax6) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Escolhe capacidade intermediária para comparação
    mid_idx = len(capacities) // 2
    mid_capacity = capacities[mid_idx]
    
    algorithms = ['Recursivo', 'Memoização', 'Prog. Dinâmica']
    times_comparison = [
        results['recursive']['times'][mid_idx] if results['recursive']['times'][mid_idx] else 0,
        results['memoized']['times'][mid_idx],
        results['dynamic']['times'][mid_idx]
    ]
    ops_comparison = [
        results['recursive']['operations'][mid_idx] if results['recursive']['operations'][mid_idx] else 0,
        results['memoized']['operations'][mid_idx],
        results['dynamic']['operations'][mid_idx]
    ]
    
    colors = ['#e74c3c', '#3498db', '#2ecc71']
    
    # Gráfico de barras - Tempo
    bars1 = ax5.bar(algorithms, times_comparison, color=colors, alpha=0.8, edgecolor='black')
    ax5.set_ylabel('Tempo de Execução (segundos)', fontsize=12, fontweight='bold')
    ax5.set_title(f'Comparação de Tempo (Capacidade = {mid_capacity})', 
                  fontsize=14, fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # Adiciona valores nas barras
    for bar in bars1:
        height = bar.get_height()
        if height > 0:
            ax5.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.6f}s',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Gráfico de barras - Operações
    bars2 = ax6.bar(algorithms, ops_comparison, color=colors, alpha=0.8, edgecolor='black')
    ax6.set_ylabel('Número de Operações', fontsize=12, fontweight='bold')
    ax6.set_title(f'Comparação de Operações (Capacidade = {mid_capacity})', 
                  fontsize=14, fontweight='bold')
    ax6.grid(True, alpha=0.3, axis='y')
    ax6.set_yscale('log')
    
    # Adiciona valores nas barras
    for bar in bars2:
        height = bar.get_height()
        if height > 0:
            ax6.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('unbounded_knapsack_bar_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Gráfico de barras salvo como 'unbounded_knapsack_bar_comparison.png'")
    
    plt.show()


def print_summary_table(capacities, results):
    """
    Imprime uma tabela resumo dos resultados
    """
    print("\n" + "="*100)
    print("TABELA RESUMO DE RESULTADOS")
    print("="*100)
    print(f"{'Capacidade':<12} {'Algoritmo':<25} {'Tempo (s)':<15} {'Operações':<15} {'Valor':<10}")
    print("-"*100)
    
    for i, cap in enumerate(capacities):
        # Recursivo
        if results['recursive']['times'][i] is not None:
            print(f"{cap:<12} {'Recursivo Simples':<25} "
                  f"{results['recursive']['times'][i]:<15.6f} "
                  f"{results['recursive']['operations'][i]:<15} "
                  f"{results['recursive']['values'][i]:<10}")
        else:
            print(f"{cap:<12} {'Recursivo Simples':<25} {'FALHOU':<15} {'N/A':<15} {'N/A':<10}")
        
        # Memoizado
        print(f"{'':<12} {'Recursivo + Memoização':<25} "
              f"{results['memoized']['times'][i]:<15.6f} "
              f"{results['memoized']['operations'][i]:<15} "
              f"{results['memoized']['values'][i]:<10}")
        
        # Programação Dinâmica
        print(f"{'':<12} {'Programação Dinâmica':<25} "
              f"{results['dynamic']['times'][i]:<15.6f} "
              f"{results['dynamic']['operations'][i]:<15} "
              f"{results['dynamic']['values'][i]:<10}")
        print("-"*100)
    
    print("\n" + "="*100)
    print("ANÁLISE DE COMPLEXIDADE")
    print("="*100)
    print("• Recursivo Simples: Complexidade exponencial O(n^W) - muito lento para grandes entradas")
    print("• Recursivo + Memoização: Complexidade O(n*W) - evita recalcular subproblemas")
    print("• Programação Dinâmica: Complexidade O(n*W) - solução iterativa eficiente")
    print("  (onde n = número de itens, W = capacidade da mochila)")
    print("="*100)


if __name__ == "__main__":
    # Executa os benchmarks
    capacities, results = run_benchmarks()
    
    # Imprime tabela resumo
    print_summary_table(capacities, results)
    
    # Gera os gráficos
    print("\n" + "="*70)
    print("Gerando gráficos comparativos...")
    print("="*70)
    generate_graphs(capacities, results)
    
    print("\n✅ Benchmark completo!")
    print("\nArquivos gerados:")
    print("  📊 unbounded_knapsack_comparison.png")
    print("  📊 unbounded_knapsack_bar_comparison.png")
