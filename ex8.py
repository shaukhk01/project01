class P:
    a = 10
    def __init__(self):
        self.b = 20
class C(P):
    c = 30
    def __init__(self):
        super().__init__()
        self.d = 40
obj = C()
print(obj.a,obj.d,obj.b)
