import re
def main():
    matched = re.finditer('a?','abcdabdk')
    for m in matched:
        print(m.start(),'--',m.group())
main()
