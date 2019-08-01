class p:
    a = 10
    def __init__(self):
        self.b = 20
    @staticmethod
    def main():
        print('parent class method')
class Q(p):
    c = 30
    def __init__(self):
        self.d = 40
        super().__init__()
    @classmethod
    def main0(cls):
        print('child class method')
o = Q()
o.main0()
o.main()
print(o.a,o.b,o.c,o.d)
