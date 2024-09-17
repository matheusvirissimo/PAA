def bubble_sort(array): ## recebe uma lista

    ## loop de fora para iterar a lista n vezes
    for n in range(len(array) - 1, 0, -1):
        for i in range(n):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp 
    return array

array = [39, 12, 18, 85, 72, 10, 2, 18]
print("Array desorganizado")
print(array)

bubble_sort(array)

print("Array organizado:")
print(array)