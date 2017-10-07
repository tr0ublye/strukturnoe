n= input()
b= int(input("vvedi b: "))
m=1
for i in n:
    if int(i) !=0:
        m*=int(i)
if m<b :
    print("b>m: true")
    print("m=",m)
else :
    if (m>b) :
        print ("b<m: true")
        print("m=",m)
    else :
        print ("b=m",b,m)
