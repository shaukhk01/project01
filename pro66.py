import re
def main():
    s1 = input('Enter a mobile number.')
    s2 = re.search('[789]\d{9}',s1)
    if s2 !=None:
        print('it is mobile number.')
    else:
        print('it is not mobile number.')
main()
