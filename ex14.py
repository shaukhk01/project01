class Car:
    brand = 'INNOVA'
    def __init__(self,name,model,color):
        self.name = name
        self.model= model
        self.color= color
    def main(self):
        print('specification.')
        print('Brand Name:',self.brand)
        print(' ' * 5,self.name)
        print(' ' * 5,self.model)
        print(' ' * 5,self.color)
    def string(self):
        print('Delivery:')
        print('-'*30)
class Customer:
    def __init__(self,Cname,Address,Pincode,car):
        self.Name = Cname
        self.Cadd = Address
        self.zipcod= Pincode
        self.car = car
    def main0(self):
        self.car.main()
        self.car.string()
        print(self.Name)
        print(self.Cadd)
        print(self.zipcod)
        print('---------------------------------')

obj = Car('Inova2.5','2.5v','red')
emp = Customer('ANNIE','144,UK STREET LINE,TAXES UK',550844,obj)
emp.main0()
