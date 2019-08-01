import re
def main():
    matched = re.finditer('a{2}','abcdeaakkkaa')
    for m in matched:
        print(m.start(),'--',m.group())
main()
