def selection_sort(arr):
    # Percorre o array
    for i in range(len(arr)):
        # Assume que o menor elemento é o primeiro da parte não ordenada
        min_idx = i
        # Percorre a parte não ordenada do array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort_with_print(arr):
    print("Array antes da ordenação (Selection Sort):", arr)
    selection_sort(arr)
    print("Array depois da ordenação (Selection Sort):", arr)
    return arr

# # Array de exemplo
# array = [39, 12, 18, 85, 72, 10, 2, 18]
# selection_sort_with_print(array)
