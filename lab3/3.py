import math
def f1():
    x=0.1
    while x<2.5:
        print(x, "\t", x**2+2*math.pi*math.cos(math.pi*x))
        x+=0.2
    
def main(): 
    f1() 
    return 0
if __name__ == '__main__':
    main()

