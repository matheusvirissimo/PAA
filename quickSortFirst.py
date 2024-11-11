def quicksort_first_pivot(arr):
    # Stack para armazenar os índices dos subarrays
    stack = [(0, len(arr) - 1)]

    while stack:
        # Desempilha os limites do subarray atual
        left, right = stack.pop()

        if left < right:
            # Define o primeiro elemento como pivô
            pivot = arr[left]
            i = left + 1
            j = right

            while True:
                while i <= j and arr[i] <= pivot:
                    i += 1
                while i <= j and arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                else:
                    break

            # Coloca o pivô na posição correta
            arr[left], arr[j] = arr[j], arr[left]

            # Adiciona as novas porções à pilha para serem ordenadas
            stack.append((left, j - 1))
            stack.append((j + 1, right))

    return arr

# Função com print para visualização
def quicksort_first_pivot_with_print_stack(arr):
    print("Array antes da ordenação (pivô = primeiro elemento):", arr)
    sorted_arr = quicksort_first_pivot_stack(arr)
    print("Array depois da ordenação (pivô = primeiro elemento):", sorted_arr)
    return sorted_arr

# # Array de exemplo
# array = [39, 12, 18, 85, 72, 10, 2, 18]
# quicksort_first_pivot_with_print_stack(array)
