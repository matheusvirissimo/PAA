def shell_sort(arr):
    # Inicializamos o gap como sendo metade do tamanho da lista
    gap = len(arr) // 2

    # Continuamos enquanto o gap for maior que 0
    while gap > 0:
        # Usamos o Insertion Sort modificado para ordenar os elementos separados pelo gap
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Compara elementos com a distância gap e faz a troca, se necessário
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        # Reduzimos o gap pela metade
        gap //= 2

def shell_sort_with_print(arr):
    print("Array antes da ordenação (Shell Sort):", arr)
    shell_sort(arr)
    print("Array depois da ordenação (Shell Sort):", arr)
    return arr

# Array de exemplo
array = [39, 12, 18, 85, 72, 10, 2, 18]
shell_sort_with_print(array)
