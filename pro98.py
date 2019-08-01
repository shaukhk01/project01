def main():
    class Suzuki:
        brand = 'SUZUKI'
        def __init__(self,Engine,Cc,No_of_cylinder,power):
            self.Engine = Engine
            self.Cc     = Cc
            self.No_of_cylinder = No_of_cylinder
            self.power  = power
        @staticmethod
        def comment():
            print(' '*5,'Car Details:')
            print('*'*23)
    class ex_feature(Suzuki):
        def __init__(self,Mileage,Tank_cap,Tyre_type):
            self.Mileage   = Mileage
            self.Tank_cap  = Tank_cap
            self.Tyre_type = Tyre_type

            super().__init__('K-Series Petrol Engine With VVT'
                    ,'1197 CC',4,'82 bhp@600 rpm')
            super().comment()
            self.carinfo()
        def Feature(self):
            print(' Mileage :',self.Mileage)
            print(' Tank_cap:',self.Tank_cap)
            print(' Tyre_type:',self.Tyre_type)
            print()
            #self.carinfo()
        def call_emp_fun(self):
            print(' '*5,'Employee Details:')
            self.empinofo()
            #self.carinfo()
    class Emp(ex_feature):
        def __init__(self,Empno,Ename,Deptno):
            self.Empno = Empno
            self.Ename = Ename
            self.Deptno= Deptno
            super().__init__('22.00 kmpl','37.00','Tubeless')
            super().call_emp_fun()
        def empinofo(self):
            print('*' * 23)
            print(' Empno   : ',self.Empno)
            print(' Ename   : ',self.Ename)
            print(' Deptno  : ',self.Deptno)
        def carinfo(self):
            print(' Brand   :',self.brand)
            print(' Engine  :',self.Engine)
            print(' CC      :',self.Cc)
            print(' cylinder:',self.No_of_cylinder)
            print(' power   :',self.power)
            self.Feature()

    o = Emp('17633','Bridget','10')

main()


