class p:
    a = 10
    def __init__(self):
        self.b = 20
    def main(self):
        print('parent instance method')
    @classmethod
    def main0(cls):
        print('parent class method')
    @staticmethod
    def main1():
        print('parent staticmethod')
class C(p):
    pass

o = C()
print(o.a)
print(o.b)
o.main()
o.main1()
o.main0()
