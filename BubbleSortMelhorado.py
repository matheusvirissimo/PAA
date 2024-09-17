def bubble_sort_melhorado(array):
    n = len(array)

    for i in range (n-1, 0, -1):
        troca = False

        for j in range (i):
            if array[j] > array[j+1]:
                troca = True
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        if not troca:
            break

array = [39, 12, 18, 85, 72, 10, 2, 18]
print("Array desorganizado")
print(array)

bubble_sort_melhorado(array)

print("Array organizado:")
print(array)
            