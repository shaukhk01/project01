import re
count = 0
match = re.finditer('ab','abbcdedab')
for m in match:
    count +=1
    print(m.start(),'---',m.end(),'---',m.group())
print('no of occurence',count)
