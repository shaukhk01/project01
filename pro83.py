class vehicle:
    brand = 'INNOVA'
    def __init__(self,name,model,color,price):
        self.name  = name
        self.model = model
        self.color = color
        self.price = price
    def main(self):
        print('Details about car:')
class Emp:
    def __init__(self,Empno,Ename,deptno,name,model,color,price):
        self.vehicle = vehicle(name,model,color,price)
        self.Empno  = Empno
        self.Ename  = Ename
        self.deptno = deptno

    def getinfo(self):
        print('Employee details:')
        print('-'*50)
        print('-'*50)
        print('Employee number: ',self.Empno)
        print('Employee name: ',self.Ename)
        print('Employee deptno: ',self.deptno)
        print('-'*50)
        print('-'*50)
        self.vehicle.main()
        print(self.vehicle.brand,self.vehicle.name,self.vehicle.model,self.vehicle.color,self.vehicle.price,sep=',')
#fun_car =  vehicle('Inov5','2.5v','blue','230021')

emp_data = Emp('77653','ANNIE','10','Inov5','2.5v','blue','230021')
emp_data.getinfo()
