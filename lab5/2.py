import math 

X = []
Y = []
R = []
n = 17
x = n

print("Введите массив X: ")
for i in range(0, n):
    X.append(int(input()))
    if math.cos(X[i]) > 0:
        Y.append(pow(X[i], 3) - 7.5)
    else:
        Y.append(pow(X[i], 2) - 5 * math.exp(math.sin(X[i])))
print("Упорядоченный массив Y: ")

m = n-1
while m > 0:
    for i in range(m):
        if Y[i] > Y[i+1]:
            x = Y[i]
            Y[i] = Y[i+1]
            Y[i+1] = x
    m -= 1

for i in range(0, n):
    print(Y[i])
print("Упорядоченный массив X: ")

m = n-1
while m > 0:
    for i in range(m):
        if X[i] < X[i+1]:
            x = X[i]
            X[i] = X[i+1]
            X[i+1] = x
    m -= 1

for i in range(0, n):
    print(X[i])
print("Массив R: ")

for i in range(0, n, 2):
    R.append(X[i])
    R.append(Y[i])

for i in range(0, n+1):
    print(R[i])
