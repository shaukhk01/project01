import re
def main():
    match = re.finditer('[a-zA-Z]','ABCabcDfg12')
    for m in match:
        print(m.start(),'--',m.group())
main()
