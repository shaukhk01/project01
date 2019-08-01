class car:
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def main(self):
        print('name {}\nmode {}\ncolor {}'.format(self.name,self.model,self.color))
class person:
    def __init__(self,name,deptno):
        self.name = name
        self.deptno  = deptno
class Emp(person):
    def __init__(self,empno,name,deptno,car):
        self.empno = empno
        self.car = car
        super().__init__(name,deptno)
    def getinfo(self):
        print('Empno',self.empno)
        print('Name',self.name)
        print('deptno',self.deptno)
        self.car.main()

c = car('Innova','2.5v','Red')
e = Emp('78321','ANNIE','20',c)
e.getinfo()
