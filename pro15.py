import re
def main():
    matched = re.finditer('.','Hel@lo123wor#l d')
    for m in matched:
        print(m.start(),'--',m.group())
main()
