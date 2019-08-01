class Engine:
    a = 10
    def __init__(self):
        self.b = 20
    def main(self):
        print('Engine Functionality..')
class Car:
    def __init__(self):
        self.engine = Engine()
    def m2(self):
        print('Car using Engine Functionality...')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.main()
obj = Car()
obj.m2()
