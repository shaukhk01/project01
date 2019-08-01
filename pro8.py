import re
def main():
    count = 0
    matched = re.finditer('ab','aabcdefbckhax')
    for m in matched:
        print(m.start(),'--',m.group())
        count +=1
    print('no of occurence',count)
main()
