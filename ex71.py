a = int(input('Enter a 1st number.'))
b = int(input('Enter a 2nd number.'))
c = int(input('Enter a 3rd number.'))

min = a if a<b and a<c else b if b<c else c
print(min)
a = int(input('Enter 1st number.'))
b = int(input('Enter 2d number.'))
c = int(input('Enter 3rd number.'))

max = a if a>b and a>c else b if b>c else c
print(max)
