import re
def main():
    matched = re.finditer('[a-z]','hello WORLD')
    for m in matched:
        print(m.start(),'---',m.group())
main()
