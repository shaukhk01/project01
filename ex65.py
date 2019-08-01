class car:
    brand = 'INNOVA'
    def __init__(self,model,power,price):
        self.model = model
        self.power = power
        self.price = price
    @staticmethod
    def header():
        print('Employee details:')
class Emp(car):
    def __init__(self,Empno,Ename,deptno,model,power,price):
        self.Empno = Empno
        self.Ename = Ename
        self.deptno= deptno
        super().__init__(model,power,price)
    def info(self):
        self.header()
        print('Empno: ',self.Empno)
        print('Ename: ',self.Ename)
        print('deptno: ',self.deptno)
        print()
        print('Car details:')
        print('model',self.model)
        print('power',self.power)
        print('print',self.price)
        

c = Emp(76432,'ANNIE',10,'2.5v','26cc',2500323)
c.info()

