import re
def main():
    s = re.split('\.','www.google.com')
    for x in s:
        print(x)
main()
