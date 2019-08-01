class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def main(self):
        print('name:{}\nmodel:{}\ncolor:{}'.format(self.name,self.model,self.color))
class Emp:
    def __init__(self,Empno,Ename,deptno,car):
        self.Empno = Empno
        self.Ename = Ename
        self.deptno= deptno
        self.car = car
    def Einfo(self):
        print(self.Empno,'\n',self.Ename,'\n',self.deptno)
        self.car.main()
c = Car('INNOVA','2.5V','red')
e = Emp(2183,'ANNIE',10,c)
e.Einfo()

