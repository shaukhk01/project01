def main():
    class Honda:
        brand = 'Honda'
        def __init__(self,model,cc,kmpl,kg):
            self.model = model
            self.cc    = cc
            self.kmpl  = kmpl
            self.kg    = kg
        def features(self):
            print('Honda bike Feature.')
            print('*' * 10)
    class Emp(Honda):

        def __init__(self,Empno,Ename,Deptno,model,cc,kmpl,kg):
              super().__init__(model,cc,kmpl,kg)
              self.Empno  = Empno
              self.Ename  = Ename
              self.Deptno = Deptno
              self.features()
        def empinfo(self):
            print('BRAND:',self.brand,self.model,',',self.cc,'cc,',self.kmpl,'kmpl,',self.kg,'kg,')
            print()
            self.info()
            print('Empno: ',self.Empno)
            print('Ename: ',self.Ename)
            print('Deptno: ',self.Deptno)
        def info(self):
            print('Employee Details:')
            print('*'*10)

    o = Emp(87632,'ANNIE',10,'Activa 5G','109.19',60,109)
    o.empinfo()
main()





