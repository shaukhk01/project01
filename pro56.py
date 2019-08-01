import re
def main():
    s1 = input('Enter a pattern to check.')
    s1 = re.fullmatch(s1,'Learning python')
    if s1 !=None:
        print('Yes it is matched.')
    else:
        print('Yest it is not matched')
main()
