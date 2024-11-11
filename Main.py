import BubbleSort, BubbleSortMelhorado, quickSortFirst, quickSortMiddle ## por troca
import insertionSort, shellSort ## por inserção 
import selectionSort, heapSort, mergeSort # por seleção

import time
import matplotlib.pyplot as plt #install matplotlib
import pandas as pd # install pandas, instal openpyxl
import random
import sys

sys.setrecursionlimit(10**5)

def vetor_aleatorio(num):
    return [random.randint(1, num) for _ in range(num)]

def vetor_ordenado(num):
    return list (range(1, num + 1))

def vetor_invertido(num):
    return list(range(num, -1, -1))

def medir_tempo(sort_func, arr):
    ini = time.perf_counter()
    sort_func(arr)
    fim = time.perf_counter()
    return fim - ini

def plot_graph(df, titulo, nome_arquivo):
    plt.figure(figsize=(12, 8))
    plt.title(titulo)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)
    for algo_nome in df.columns[1:]:
        plt.plot(df["Tamanho do Vetor"], df[algo_nome], label=algo_nome, linewidth=3)
    plt.legend()
    plt.savefig(nome_arquivo)
    plt.close()

def main():
    algoritmos_ordenacao = {
        # "Bubble Sort": BubbleSort.bubble_sort,
        # "Bubble Sort Melhorado": BubbleSortMelhorado.bubble_sort_melhorado,
        # "Quick Sort com pivô no INÍCIO": quickSortFirst.quicksort_first_pivot,
        # "Quick Sort com pivô no MEIO": quickSortMiddle.quicksort_middle_pivot,
        # "Insertion Sort": insertionSort.insertion_sort,
        # "Shell Sort": shellSort.shell_sort,
        # "Selection Sort": selectionSort.selection_sort,
        # "Heap Sort": heapSort.heap_sort,
        # "Merge Sort": mergeSort.merge_sort,
    }

    tam_vetor = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]

    for algo_nome, algo_func in algoritmos_ordenacao.items():
        resultados = {"Tamanho do Vetor": tam_vetor}
        for escrever_nome, gerar_func in [("Vetor Aleatório", vetor_aleatorio),
                                          ("Vetor Ordenado", vetor_ordenado),
                                          ("Vetor Inversamente Ordenado", vetor_invertido)]:
            tempo_algoritmos = []
            for num in tam_vetor:
                arr = gerar_func(num)
                tempo_exec = medir_tempo(algo_func, arr)
                tempo_algoritmos.append(tempo_exec)
            resultados[escrever_nome] = tempo_algoritmos
        df = pd.DataFrame(resultados)
        df.to_excel(f"{algo_nome}.xlsx")
        plot_graph(df, f"Algoritmo de Ordenação - {algo_nome}", f"{algo_nome}.png")

if __name__ == "__main__":
    main()