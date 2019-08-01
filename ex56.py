class A:
    pass
class B(A):
    pass
class C(B):
    pass
x = C()
print(isinstance(x,B),isinstance(x,A))
print(isinstance(x,C))
