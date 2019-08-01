class P:
    a = 888
    def main(self):
        self.x = 200
class C(P):
    def __init__(self):
        super().main()
        print(self.x)
        print(super().a)
c = C()
