class Space:
    def __init__(self):
        self.name1 = 'MARS'
        self.name2 = 'MOON'
        self.name3 = 'JUPI'
    def main(self):
        print('Planet name.')
class Earth:
    def __init__(self):
        self.space = Space()
    def main0(self):
        self.space.main()
        print(self.space.name1)
        print(self.space.name2)
        print(self.space.name3)
obj = Earth()
obj.main0()
    

