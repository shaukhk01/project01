class p:
    a = 10
    def __init__(self):
        self.b = 20
class c(p):
    c = 30
    def __init__(self):
        self.d = 40
    def main(self):
        print(self.a,self.c)
        super().__init__()
        print(self.d,self.b)
C = c()
C.main()
