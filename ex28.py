class p:
    z = 99
    def __init__(self):
        self.x = 10
class c(p):
    def __init__(self):
        self.y = 30
        #super().__init__()
        #print(super().x)
        print(self.x)
o = c()
