import re
def main():
    matched = re.finditer('\D','1234Hello5678')
    for m in matched:
        print(m.start(),'---',m.group())
main()
