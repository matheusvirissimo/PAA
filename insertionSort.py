def insertion_sort(arr):
    # Percorre o array da segunda posição até o final
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move os elementos do array que são maiores que a chave uma posição para frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertion_sort_with_print(arr):
    print("Array antes da ordenação (insertion sort):", arr)
    insertion_sort(arr)
    print("Array depois da ordenação (insertion sort):", arr)
    return arr

# Array de exemplo
# array = [39, 12, 18, 85, 72, 10, 2, 18]
# insertion_sort_with_print(array)
