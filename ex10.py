


class A:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
class B(A):
    def __init__(self,job,dept):
        self.job = job
        self.dept = dept
        super().__init__(name,age)
obj = B('Oracle',30,'Annie',33)
