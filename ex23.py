import sys
class Test:
    pass
t1 = Test()
t2 = t1
t3 = t2
t4 = t3
print(sys.getrefcount(t4))
