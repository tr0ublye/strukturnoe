class drob:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def procennt(self):
        return (self.x / self.y)*100
    def sumcif(self):
        mult = 1
        summa = 0
        while self.y > 0:
            if self.y % 10 != 0:
                mult = mult * (self.y % 10)
            summa = summa + self.y % 10
            self.y = self.y // 10
        return summa

a = float(input("vvedi 4islitel: "))
b = float(input("vvedi znamenatel: "))
cl = drob(a, b)

print(cl.procennt())
print(cl.sumcif())
