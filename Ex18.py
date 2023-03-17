# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
numberN = int(input('Введите длину массива: '))
arr = []
for i in range(numberN):
    arr.append(int(input(f'Введите {i} элемент: ')))
print(arr)
numberX = int(input('Введите искомое число: '))
min = abs(numberX - arr[0])
flag = 0
for i in range(1, numberN):
    if abs(numberX-arr[i])<min:
        min = abs(numberX-arr[i])
        flag = i
        result = arr[i]
print(f'Ближе всего к искомому числу "{numberX}" = {flag} элемент (= "{result}")')
