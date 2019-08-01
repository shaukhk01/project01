import re
def main():
    s = re.subn('[a-z]','#','abc1234abc')
    print(s)
    print('The Result of string',s[0])
    print('The no of occurences',s[1])
main()

