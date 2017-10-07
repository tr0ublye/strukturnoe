s = str(input("Введите строку "))
b = str()
L = list(s)
L.reverse()
for i in range(0, len(s)):
    b += L[i]
print(b)
