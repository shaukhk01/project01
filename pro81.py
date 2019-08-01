class a:
    def m1(self):
        print('class a method')
class b:
    def m2(self):
        print('class b method)')
class c(b,a):pass
o = c()
o.m1()
