class Engine:
    def __init__(self,Name,Model):
        self.name = Name
        self.model= Model
    def main(self):
        pass
        #print('*' * 50)
class Car(Engine):
    def __init__(self,Color,CC,Price,Name,Model):
        self.color = Color
        self.cc    = CC
        self.Price = Price
        super().__init__(Name,Model)
    def main(self):
        print('*' * 50)
    def main0(self):
        print('Name :',self.name, '  * ')
        print('Model:',self.model,'  * ')
        print('Color',self.color, '  * ')
        print('CC   :',self.cc,   '  * ')
        print('Price:',self.Price,'  * ')
class Emp:
    def __init__(self,Empno,Ename,Deptno):
        self.empno = Empno
        self.ename =Ename
        self.Deptno = Deptno
    def main(self):
        print('Employee number  :',self.empno)
        print('Employee name    :',self.ename)
        print('Employee departno:',self.Deptno)
Object = Car('Red','13cc','260000','Innova','2.5v')
Object.main()
Emp_ob = Emp(74723,'ANNIE',30)
Emp_ob.main()
Object.main()
Object.main0()
