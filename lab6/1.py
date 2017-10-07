import math
class task1:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def gip(self):
        return math.sqrt(self.x**2 + self.y**2)

a = float(input("vvedi a: "))
b = float(input("vvedi b: "))
cl = task1(a, b)

print(cl.gip())
