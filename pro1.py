s1 = input('Enter a string.')
output1=output2=output3 = ''
for x in s1:
    if x.isalpha():
        output1 +=x
    else:
        output2 +=x
for x in sorted(output1):
   output3 +=x
print(output3 +''.join(sorted(output2)))
