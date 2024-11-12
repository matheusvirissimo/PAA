def quicksort_middle_pivot(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            # Escolhe o pivô como o elemento central
            middle = (low + high) // 2
            pivot_index = partition(arr, low, high, middle)
            
            # Empilha os sub-arranjos para ordenação
            stack.append((low, pivot_index - 1))  # Elementos menores que o pivô
            stack.append((pivot_index + 1, high))  # Elementos maiores que o pivô

    return arr

def partition(arr, low, high, pivot_index):
    pivot = arr[pivot_index]
    # Mover o pivô para o início temporariamente
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    
    left = low + 1
    right = high

    while True:
        # Avança left enquanto os elementos forem menores ou iguais ao pivô
        while left <= right and arr[left] <= pivot:
            left += 1
        # Retrocede right enquanto os elementos forem maiores que o pivô
        while left <= right and arr[right] > pivot:
            right -= 1
        if left <= right:
            # Troca os elementos se left ainda é menor que right
            arr[left], arr[right] = arr[right], arr[left]
        else:
            # Quebra o loop quando left ultrapassar right
            break

    # Coloca o pivô na posição correta
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Exemplo de uso
#array = [39, 12, 18, 85, 72, 10, 2, 18]
#print("Array antes da ordenação:", array)
#sorted_array = quicksort_iterative_middle_pivot(array)
#print("Array depois da ordenação:", sorted_array)
