class a:
    def __init__(self,name):
        self.name = name
    def hi(self):
        print('Hello world')
class b(a):
    def __init__(self):
        pass
    def hi(self):
        print(self.name)
y = b('JAMES')
y.i()
