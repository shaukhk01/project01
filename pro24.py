import re
def main():
    matched = re.finditer('#$','Hector#')
    for m in matched:
        print(m.start(),'--',m.group())
main()
