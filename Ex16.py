# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
numberN = int(input('Введите длину массива: '))
arr = []
for i in range(numberN):
    arr.append(input(f'Введите {i} элемент: '))
print(arr)
numberX = input('Введите искомое число: ')
result = 0
for i in range(numberN):
    if arr[i] == numberX:
        result = result+1
print(f'Кол-во совпадений = {result}')