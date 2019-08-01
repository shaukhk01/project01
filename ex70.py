import re
count = 0
matcher = re.finditer('ab','abcabcab')
for m in matcher:
    count +=1
    print(m.start(),'...',m.end(),'...',m.group())
print('no of count',count)
