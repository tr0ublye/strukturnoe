s = input('Введите предолжение ')
arr = s.split()

for i in range(len(arr)):
    bol = 1
    k = i-1
    while k >= 0 and bol:
        if arr[i] == arr[k]:
            bol = 0
        k -= 1
    if bol:
        print(arr[i])
