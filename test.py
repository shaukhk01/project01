class p:
    def __init__(self):
        pass
    def main(self):
        print('instance method')
class c(p):
    def __init__(self):
        pass
    def m(self):
        self.main()
o = c()
o.m()
