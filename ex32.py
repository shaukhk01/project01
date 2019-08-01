class C:
    brand = 'Innova'
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
    @staticmethod
    def main():
        print('product spec:')
class Emp(C):
      def __init__(self,empno,name,deptno,model,color,price):
          self.empno = empno
          self.name  = name
          self.deptno= deptno
          super().__init__(model,color,price)
      def getinfo(self):
          print('-'*20)
          print('Employee details:')
          print('-'*20)
          print('Empno',self.empno)
          print('name',self.name)
          print('deptno',self.deptno)
          print('-'*20)
          self.main()
          print('-'*20)
          print('brand',self.brand)
          print('model',self.model)
          print('color',self.color)
          print('price',self.price)
o = Emp(17542,'ANNIE',20,'2.5v','red',115033)
o.getinfo()



