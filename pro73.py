import re
def main():
    s1 = input('Enter a mail id.')
    s2 = re.fullmatch('[\w]*.@gmail.com',s1)
    if s2 !=None:
        print('valid mail id.')
    else:
        print('invalid mail id.')
main()
