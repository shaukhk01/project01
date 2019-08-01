import re
def main():
    pattern = re.compile('a')
    count = 0
    match = pattern.finditer('abcdabccdaa')
    for m in match:
        count +=1
        print(m.start(),'--',m.end(),'--',m.group())
    print('no of occurences.',count)
main()
