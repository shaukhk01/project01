import re

count = 0
b = re.compile('b')
m = b.finditer('abcdefabghkab')

for match in m:
    count +=1
    print(match.start(),'---',match.end(),'---',match.group())
print('no of occurence',count)


