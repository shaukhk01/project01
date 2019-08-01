class p:
    def main(self):
        print('superclass')
class c(p):
    def main1(self):
        print('subclass')
C = c()
C.main()
C.main1()
