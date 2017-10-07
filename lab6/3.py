import math
class task1:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def gip(self):
        return math.sqrt(self.x**2 + self.y**2)
class task2(task1):
    def __init__(self, c):
        task1.__init__(self, a, b)
        self.h = c
    def sumreb(self):
        return self.x*2 + self.y*2 + task1.gip(self)*2 + (self.h * 3)

a = float(input("katet a: "))
b = float(input("katet b: "))
c = float(input("visota prinzmi: "))

cl = task1(a, b)
cl2 = task2(c)

print(cl.gip())
print(cl2.sumreb())
