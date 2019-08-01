import re
def main():
    matched = re.finditer('a{3,3}','khakjasdaa,lkaaakjllaaaaa')
    for m in matched:
        print(m.start(),'--',m.group())
main()
