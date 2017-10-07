class drob:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def procent(self):
        return (self.x/self.y)*100
    def sumcif(self):
        mult = 1
        summa = 0
        while self.y > 0:
            if self.y % 10 != 0:
                mult = mult * (self.y % 10)
            summa = summa + self.y % 10
            self.y = self.y // 10
        return summa

class smeshdob(drob):
    def __init__(self, c):
        drob.__init__(self, a, b)
        self.cel = c
    def pred(self):
        return (self.cel*self.y + self.x) / self.y

a = float(input("vvedi 4islitel:  "))
b = float(input("vvedi znamenatel: "))
c = int(input("введи целуючасть:"))

cl = drob(a, b)
cl2 = smeshdob(c)
print(cl.procent(), "%")
print(cl.sumcif())
print(cl2.pred())
