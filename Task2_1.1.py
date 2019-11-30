class ParentArea:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Area(ParentArea):
    def calc(self):
        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area


CalcArea = Area(34,67,56)
print("Area = ",CalcArea.calc())