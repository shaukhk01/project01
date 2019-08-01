class p:
    def __init__(self):
        pass
    def m2(self):
        self.m1()

class c(p):
    def __init__(self):
        super().__init__()
        super().m2()
    def m1(self):
        print('Hell')
o = c()
