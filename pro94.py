def main():
    class uper:
        def __init__(self,Empno,Ename,deptno):
            self.Empno = Empno
            self.Ename = Ename
            self.deptno= deptno
        def info(self):
            print(self.Empno)
            print(self.Ename)
            print(self.deptno)
            print('   ','End','   ')
    class sub(uper):
        def __init__(self):
            super().__init__(78653,'Bridget',10)
            super().info()
        def ini(self):
            print('initilizin...values from sub class to super class')
    o = sub()
main()

