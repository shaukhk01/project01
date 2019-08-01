class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def main0(self):
        print('{}, {}, {}'.format(self.name,self.model,self.color))
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
class Emp(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal=esal
        self.car = car
    def main1(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)
        self.car.main0()
o = Car('INNOVA','2.5V','RED')
e = Emp('Annie',23,1231,10000,o)
e.main1()

