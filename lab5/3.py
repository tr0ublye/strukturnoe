M1 = []
M2 = []

print("Введите массив1: ")
for i in range(0, 7):
    M1.append(float(input()))
print("Введите массив2: ")
for i in range(0, 9):
    M2.append(float(input()))

C = M1 + M2
m = len(C) - 1
while m > 0:
    for i in range(m):
        if C[i] > C[i+1]:
            x = C[i]
            C[i] = C[i+1]
            C[i+1] = x
    m -= 1

print("Vассив3: ")
for i in range(0, len(C)):
    print(C[i])
