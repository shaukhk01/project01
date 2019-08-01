import re
def main():
    match = re.finditer('ab','bbbacabkhan9ab@')
    count = 0
    for m in match:
        count +=1
        print(m.start(),'--',m.end(),'--',m.group())
    print('no of occurences',count)
main()
