import random

def pr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

Mx = [[random.randint(0, 9) for j in range(8)] for i in range(7)]

pr(Mx)

for i in range(0, 8):
    l = 0
    for j in range(0, 7):
        if (Mx[j][i] % 2) != 0:
            l += 1
    print( i+1, " столбец ", l, " нечётных элементов")
