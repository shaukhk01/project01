import re
def main():
    match = re.finditer('[a-z]','ABCDEhello')
    for m in match:
        print(m.start(),'---',m.group())
main()
