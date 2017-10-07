import math
i=1
k=0
x= float(input("Vvedi x: "))
n= int(input("Vvedi n: "))
while i<=n :
    k=1+(math.cos(i*x)/(math.factorial(i)))
    i=i+1
    print(k)
    
    
