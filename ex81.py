import re
m = re.finditer('\W','world Hello1 23')
for match in m:
    print(match.start(),'--',match.group())
