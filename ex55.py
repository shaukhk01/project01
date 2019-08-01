class Robot:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hi I am ' + self.name)
class PhysicianRobot(Robot):
    pass
x = Robot('Marvin')
y = PhysicianRobot('James')
y.say_hi()
print(isinstance(x,PhysicianRobot),isinstance(y,Robot))
print(type(y) == Robot)
print(type(x) == Robot)
