import re
m = re.finditer('[^a-z]','abdABDklml')
n = re.finditer('[A-Z]','ABCD12345EFG')
for match in m:
    print(match.start(),'--',match.group())
for mat in n:
    print(mat.start(),'---',mat.group())
