class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def info(self):
        print('car name:{} ,mode no:{} ,color:{}'.format(self.name,self.model,self.color))
class customer:
    def __init__(self,ename,eno,car):
        self.ename = ename
        self.eno   = eno
        self.car = car
    def main(self):
        print('Employee name:',self.ename)
        print('Employee id',self.eno)
        self.car.info()
obj = Car('Ferari','F7','Red')
cust = customer('BRIDGET','101',obj)
cust.main()
