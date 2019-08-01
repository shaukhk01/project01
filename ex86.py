import re
s = input('Enter a pattern to check')
m = re.search(s,'hectorAnnieBridget')
if m !=None:
    print('pattern is available.')
    print(m.start(),'--',m.end(),'--',m.group())
