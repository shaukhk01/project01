class P:
    a = 888
    def __init__(self):
        self.x = 20
class C(P):
    a = 777
    def __init__(self):
        super().__init__()
        self.x = 30
    def main(self):
        print(super().a)
        print(self.x)
c = C()
c.main()
