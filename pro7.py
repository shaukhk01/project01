import re
pattern = re.compile('a')
match = pattern.finditer('aabcbacccbaaa')
count = 0
for m in match:
    count +=1
    print(m.start(),'--',m.end(),'--',m.group())

print('no of occurence',count)
