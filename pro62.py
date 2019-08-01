import re
def main():
    s1 = re.split('\.','www.google.com')
    print(s1)
    for s2 in s1:
        print(s2)
main()
