class person:
    def __init__(self,name,deptno):
        self.name = name
        self.deptno= deptno
class emp(person):
    def __init__(self,Empno,name,sal,deptno):
        super().__init__(name,deptno)
        self.Empno = Empno
        self.salary= sal
    def __str__(self):
        return 'Empno: {}\nname: {}\nsalary: {}\ndeptno: {}'.format(self.Empno,self.name,self.salary,self.deptno)

c = emp(Empno = '12343',name='ANNIE',sal=1000,deptno=20)
print(c)
