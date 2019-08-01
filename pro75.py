def main():
    class robot:
        def __init__(self,name):
            self.name = name
        def hi_say(self):
            print('Hi i am '+self.name)
    class machine(robot):
        def say_hi(self):
            print(self.name + 'takes care you')
    human = machine('Annie')
    human.say_hi()
main()
