class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def main(self):
        print('Car name {},Model {},Color {}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self,ename,empno,car):
        self.ename = ename
        self.empno = empno
        self.car   = car
    def main0(self):
        print(self.ename)
        print(self.empno)
        self.car.main()
c = Car('Innova','2.5v','Red')
e = Employee('Annie',110,c)
e.main0()

