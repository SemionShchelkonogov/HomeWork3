# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint

list = [randint(1,21) for i in range(int(input()))]

print(list)
num = int(input())
right = list[0]

for i in list:
    if abs(num - i) < abs(num - right):
        right = i
print(right)