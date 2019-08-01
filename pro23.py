import re
def main():
    matched = re.finditer('^@','@gmail.com')
    for m in matched:
        print(m.start(),'--',m.group())
main()
