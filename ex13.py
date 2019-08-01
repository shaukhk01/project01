class pc:
    brand = 'DELL'
    def __init__(self):
        self.hw   = 'intel'
        self.hd   = '500GB'
        self.ram   = '8GB'
        self.cpu   = 'i3'
    def main(self):
        print('Configuration.')
class config:
    def __init__(self):
        self.conf = pc()
    def main0(self):
        print('Brand name: ',self.conf.brand)
        self.conf.main()
        print(' ' * 10,self.conf.hw)
        print(' ' * 10,self.conf.hd)
        print(' ' * 10,self.conf.ram)
        print(' ' * 10,self.conf.cpu)

obj = config()
obj.main0()
