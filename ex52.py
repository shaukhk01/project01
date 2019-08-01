class Engine:
    n = 'TESLA'
    def __init__(self):
        self.part = '9v32'
class car:
    def __init__(self):
        self.E = Engine()
        self.model = 'T53'
    def main(self):
        print(self.E.n)
        print(self.model)
        print(self.E.part)
e = car()
e.main()
