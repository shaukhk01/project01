import re
s = input('Enter a pattern to check')
m = re.match(s,'abcdefg')
if m !=None:
    print('match is available')
    print(m.start(),'--',m.end(),'---',m.group())
else:
    print('not matched')
