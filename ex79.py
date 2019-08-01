import re
m = re.finditer('a{3}','abcdefabaaa')
for x  in m:
    print(x.start(),'--',x.group())
