import re
def main():
    matched = re.finditer('a+','acdbbjl@#')
    for m in matched:
        print(m.start(),'--',m.group())
main()
