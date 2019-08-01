import re
s = input('Enter a pattern to check')
m = re.fullmatch(s,'hector')
if m !=None:
    print('Pattern matched.')
    print(m.start(),'--',m.end(),'--',m.group())
else:
    print('enter not matched')
