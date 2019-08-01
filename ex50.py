class P:
    def main(self,x):
        self.x = x
class C(P):
    pass
c = C()
c.main(888)
print(c.x)
