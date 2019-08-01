import re
count = 0
pattern = re.compile('ab')
mather  = pattern.finditer('bbcb')
for match in mather:
    count +=1
    print(match.start(),'...',match.end(),'..',match.group())
    print('the number of occurence.',count)
    print('Hello')


