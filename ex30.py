class P:
    def __init__(self):
        self.a = 20
class C(P):
     def __init__(self):
         self.a = 50
         super().__init__()
         print(self.__dict__)
o = C()
