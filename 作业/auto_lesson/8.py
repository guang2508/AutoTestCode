class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        per=self.a+self.b+self.c
        return per
    def area(self):
        p=self.perimeter()/2
        s=(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return s
aaa=Triangle(3,3,3)
print(aaa.perimeter())
print(aaa.area())