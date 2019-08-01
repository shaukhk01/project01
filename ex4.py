class Computer:
    def __init__(self,Brand,Color,HD,Ram,Cpu):
        self.brand = Brand
        self.color = Color
        self.hdisk = HD
        self.ram   = Ram
        self.Cpu   = Cpu
    def info(self):
        
        print('Brand {}, Color {}, H/D {}, Ram {}, Cpu {}'.format(self.brand,self.color,self.hdisk,self.ram,self.Cpu))

class Emp:
    def __init__(self,Empno,Ename,Deptno,Pc):
        self.id = Empno
        self.name = Ename
        self.Deptno = Deptno
        self.pc = Pc
    def show(self):
        print('Empno',self.id)
        print('Ename',self.name)
        print('Deptno',self.Deptno)
        self.pc.info()
send = Computer('DELL','Black','500GB','4GB','i5')
send_emp = Emp(764,'ANNIE',30,send)
send_emp.show()
