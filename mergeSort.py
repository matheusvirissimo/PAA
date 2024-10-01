def merge_sort(arr):
    if len(arr) > 1:
        # Encontra o ponto médio da lista
        mid = len(arr) // 2

        # Divide o array em duas metades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursivamente ordena cada metade
        merge_sort(left_half)
        merge_sort(right_half)

        # Variáveis de controle para a mesclagem
        i = j = k = 0

        # Mescla as duas metades de volta no array principal
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se restaram elementos no lado esquerdo
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica se restaram elementos no lado direito
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_with_print(arr):
    print("Array antes da ordenação (Merge Sort):", arr)
    merge_sort(arr)
    print("Array depois da ordenação (Merge Sort):", arr)
    return arr

# Array de exemplo
array = [39, 12, 18, 85, 72, 10, 2, 18]
merge_sort_with_print(array)
