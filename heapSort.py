def heapify(arr, n, i):
    # Inicializa o maior como sendo o nó atual
    largest = i
    left = 2 * i + 1  # filho esquerdo
    right = 2 * i + 2  # filho direito

    # Verifica se o filho esquerdo existe e se é maior que o nó atual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se o filho direito existe e se é maior que o nó atual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior elemento não for o nó atual, troca e continua heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        # Recursivamente aplica o heapify na subárvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construção do max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extração dos elementos do heap
    for i in range(n - 1, 0, -1):
        # Troca o elemento raiz (maior) com o último elemento não ordenado
        arr[i], arr[0] = arr[0], arr[i]
        # Heapifica a subárvore reduzida
        heapify(arr, i, 0)

# def heap_sort_with_print(arr):
#     print("Array antes da ordenação (Heap Sort):", arr)
#     heap_sort(arr)
#     print("Array depois da ordenação (Heap Sort):", arr)
#     return arr
