class P:
    def main(self):
        print('Parent method.')
class C(P):
    def main0(self):
        print('Child method.')

c = C()
c.main0()
c.main()

