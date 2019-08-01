class p:
    def main(self):
        print('instance method from superclass')
class c(p):
    def m(self):
        print('instance method from child class')
C = c()
C.main()
C.m()
