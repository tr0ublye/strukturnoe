from random import random
import math
s=0
N =int(input("Введите число элементов в массиве: "))
arr = [0] * N
for i in range(N):
    arr[i] = int((random() * 100)-40)
print(arr)
neg=0
k=0
for i in range(1,N):
    if arr[i]<0:
        k+=1
        neg=neg+arr[i]
sred=neg/k

m=math.ceil(math.copysign(sred, 0))
print("среднее арифметическое отрицательных: ",m)
for i in range(1,N):
    if arr[i]>0:
        p=arr[i]
        if p>m:
            s=s+p
print("сумма: ",s)
    

