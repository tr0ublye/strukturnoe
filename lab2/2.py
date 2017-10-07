import math
a= int(input("Vvedi  4islo: "))
b= int(input("Vvedi  4islo: "))
c= int(input("Vvedi  4islo: "))

if (a>0):
    a=math.pow(a,3)
else :
    a=a-a
if (b>0):
    b=math.pow(b,3)
else :
    b=b-b
if (c>0):
    c=math.pow(c,3)
else :
    c=c-c
print (a ,b ,c )
