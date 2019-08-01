import re
def main():
    s1 = input('Enter a mobile number.')
    s2 = re.fullmatch('[7-9]\d{9}',s1)
    if s2 !=None:
        print('valid mobile number.',s1)
    else:
        print('invalid number.',s2)
main()
