import re
m = re.finditer('s$','sabcdefsas')
for match in m:
    print(match.start(),'--',match.group())
