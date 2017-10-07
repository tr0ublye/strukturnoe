import math
s= int(input("vvedi summu pokupki: "))
if s<500 :
    print ("net skidona!")
else :
    
    if 1000>s>500 :
        s=s-(s/100*5)
        print("summa so skidkoi: ",s )
    else :
        if s>1000 :
            s=s-(s/10)
            print("summa so skidkoi: ",s )
            
