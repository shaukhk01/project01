class emp:
    def __init__(self,empno,ename,sal,deptno):
        self.Empno = empno
        self.Ename = ename
        self.salary= sal
        self.deptno= deptno
    def show(self):
        print('Employee number:',self.Empno)
        print('Employee Name  :',self.Ename)
        print('Employee salary:',self.salary)
        print('Employee deptno:',self.deptno)
class update:
    def main(up):
        u = input('would like to add Employee salary Y/n\n')
        if u == 'Y' or u == 'y':
            sal = int(input('Add salary.'))
            up.salary = up.salary +  sal
            up.show()
        else:
            up.show()
e = emp(87432,'ANNIE',15000,10)
update.main(e)


