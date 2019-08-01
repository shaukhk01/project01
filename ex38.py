class person:
    def __init__(self):
        self.name = 'Bridget'
        self.deptno= 10
        self.emp = self.emp()
    def main(self):
        print(self.name)
        print(self.deptno)
        self.emp.disp()
    class emp:
        def __init__(self):
            self.job = 'Oracle-dev'
        def disp(self):
            print(self.job)
o = person()
o.main()
