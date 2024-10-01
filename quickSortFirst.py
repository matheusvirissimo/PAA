def quicksort_first_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        # O pivô é o primeiro elemento
        pivot = arr[0]
        # Elementos menores que o pivô
        left = [x for x in arr[1:] if x <= pivot]
        # Elementos maiores que o pivô
        right = [x for x in arr[1:] if x > pivot]
        return quicksort_first_pivot(left) + [pivot] + quicksort_first_pivot(right)

def quicksort_first_pivot_with_print(arr):
    print("Array antes da ordenação (pivô = primeiro elemento):", arr)
    sorted_arr = quicksort_first_pivot(arr)
    print("Array depois da ordenação (pivô = primeiro elemento):", sorted_arr)
    return sorted_arr

# Array de exemplo
array = [39, 12, 18, 85, 72, 10, 2, 18]
quicksort_first_pivot_with_print(array)
