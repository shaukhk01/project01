s = 'Durga software solutions.'
data = s.split()
l1 = []
i = 0
while i<len(data):
    l1.append(data[i][::-1])
    out = ' '.join(l1)
    i +=1
print(out)
