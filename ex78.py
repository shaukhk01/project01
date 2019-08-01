import re
m = re.finditer('a{2}','abcdefab')
count = 0
for match in m:
    count +=1
    print(match.start(),'---',match.end(),'---',match.group())
print('no of occurences',count)
