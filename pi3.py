class A:
    def m1(self):
        print('parent method')
class B(A):
    def m1(self):
        print('child method')
o = B()
o.m1()
print('-'*60)

class Emp:
    '''Employee Table Information'''
    def __init__(self,brand,model,price):

        self.brand = brand
        self.model = model
        self.price = price
        print('*'*10)


    def m1(self):
        print(self.Ename)
        print(self.job)
        print(self.mgr)
        print(self.sal)
class insert(Emp):
    def __init__(self,Ename,job,mgr,sal):
        self.Ename = Ename
        self.job   = job
        self.mgr   = mgr
        self.sal   = sal
        '''super().__init__()'''
        super().m1()
class pc(Emp):
    def __init__(self,brand,model,cost):
       ''''self.brand = brand
        self.model = model
        self.cost  = cost'''
       super().__init__(brand,model,cost)
    def pcinfo(self):
        print(self.brand)
        print(self.model)
        print(self.price)

ob1 = insert('BRIDGET','JAVA','23421',230000)

ob2 = pc('DELL','inspiron15','23700')
ob2.pcinfo()

print(issubclass(Emp,pc))
