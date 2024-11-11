def quicksort_middle_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        # O pivô é o elemento central
        middle = len(arr) // 2
        pivot = arr[middle]
        # Elementos menores que o pivô
        left = [x for x in arr[:middle] + arr[middle+1:] if x <= pivot]
        # Elementos maiores que o pivô
        right = [x for x in arr[:middle] + arr[middle+1:] if x > pivot]
        return quicksort_middle_pivot(left) + [pivot] + quicksort_middle_pivot(right)

def quicksort_middle_pivot_with_print(arr):
    print("Array antes da ordenação (pivô = elemento central):", arr)
    sorted_arr = quicksort_middle_pivot(arr)
    print("Array depois da ordenação (pivô = elemento central):", sorted_arr)
    return sorted_arr

# # Array de exemplo
# array = [39, 12, 18, 85, 72, 10, 2, 18]
# quicksort_middle_pivot_with_print(array)
