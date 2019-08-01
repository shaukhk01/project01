s = 'hello world'
i = 0
l = len(s)
print('Forward direction')
while i<l:
    print(s[i],end='')
    i +=1
print()
print('Backward direction.')
a = len(s)-1
print(a)
while a>=0:
    print(s[a],end='')
    a -=1
