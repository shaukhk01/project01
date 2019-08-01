import re
def main():
    count = 0
    matched = re.finditer('a*','abcadefa')
    for m in matched:
        print(m.start(),'--',m.group())
        count +=0
    print('no of occurence',count)
main()
