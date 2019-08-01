import re
m = re.finditer('a{2,2}','aabasdfaacdefgagcaa,dekaa')
for x in m:
    print(x.start(),'--',x.group())
