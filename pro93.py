def main():
    class Emp:
        def __init__(self,Empno,Ename,deptno):
            self.Empno= Empno
            self.Ename= Ename
            self.deptno = deptno
        def m1(self):
            print(self.Empno)
            print(self.Ename)
            print(self.deptno)
    class dept(Emp):
        def __init__(self,model,cc,kml,kg):
            super().__init__(76532,'Bridget',20)
            self.model = model
            self.cc    = cc
            self.kml   = kml
            self.kg    = kg
            self.m2()
            super().m1()
        def m2(self):
            print('Honda bike Details:')
            print('*' * 10)
            print(self.model,self.cc,self.kml,self.kg)
            print()
            print('inilizing values from sub class to super class.')
    d1 = dept('Activa 5G','300 cc','60 kml','160 kg')
main()

