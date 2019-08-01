class Engine:
    a = 10
    def __init__(self):
        self.b = 20
    def main(self):
        print('Engine specific Functionality...')
class Car:
    def __init__(self):
        self.Engine = Engine()
    def main0(self):
        print('Car using Engine class Functionality')
        print(self.Engine.a)
        print(self.Engine.b)
        self.Engine.main()
obj = Car()
obj.main0()
