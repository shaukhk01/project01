class p:
    def main(self):
        print('parent class method')
class q(p):
    def main0(self):
        print('child class method')
o = q()
o.main()
o.main0()
