class Emp:
    def __init__(self,empno,ename,sal,deptno):
        self.Empno = empno
        self.Ename = ename
        self.salary= sal
        self.deptno= deptno
    def disp(self):
        print('Employee id:',self.Empno)
        print('Employee name:',self.Ename)
        print('Employee salary',self.salary)
        print('Employee deptno',self.deptno)
class Test:
    def  modify(mod):
         mod.salary = mod.salary + 150
         mod.disp()
e = Emp(7842,'ANNIE',1997,20)
Test.modify(e)

