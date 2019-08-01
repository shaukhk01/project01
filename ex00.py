s1 = input('Enter a first string.')
s2 = input('Enter a second string.')
output = ''
i,j = 0,0
while i<len(s1) or j<len(s2):
     if i <len(s1):
         output +=s1[i]
         i +=1
     if j <len(s2):
         output +=s2[j]
         j +=1
print(output)


