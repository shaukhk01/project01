import re
def main():
    count = 0
    matched = re.finditer('a','appleabba')
    for m in matched:
        print(m.start(),'--',m.group())
        count +=1
    print('no of occurenc',count)
main()
