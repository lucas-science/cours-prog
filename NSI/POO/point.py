from math import atan2, sqrt

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.rho = 0
        self.theta = 0

    def __CalculRho__(self):
        self.rho = sqrt(self.x**2+self.y**2)

    def __CalculTheta__(self):
        self.theta = atan2(self.x, self.y)
    
    def GetRho(self):
        self.__CalculRho__()
        return self.rho

    def GetTheta(self):
        self.__CalculTheta__()
        return self.theta

    def Getx(self): return self.x
    def Gety(self): return self.y

p = Point(1,1)
print(p.GetRho(),p.GetTheta())
