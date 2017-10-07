import random

def pr(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

c = []
m = int(input("Введите m "))
n = int(input("Введите n "))

Mx = [[random.randint(0, 9) for j in range(n)] for i in range(m)]
pr(Mx)
b = abs(float(input("Введите B ")))

for i in range(0, m):
    for j in range(0, n):
        if Mx[i][j] > b:
            c.append(Mx[i][j])

print("Массив с: ", c)
print("Элементов: ", len(c))
