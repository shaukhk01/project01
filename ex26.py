class animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} having {} legs'.format(name,cls.legs))
#a = animal()
#a.walk('Dog')
animal.walk('DOG')
