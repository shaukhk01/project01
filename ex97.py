s = 'learning python is very easy.'
data = s.split()
l = len(data)-1
data_list = []
while l>=0:
    data_list.append(data[l])
    l -=1
print(' '.join(data_list))

