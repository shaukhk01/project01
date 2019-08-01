import re
def main():
    s = input('Enter a matching string.')
    m = re.fullmatch(s,'Hello world')
    if m !=None:
        print('fullmatch is complete.')
        print(m.group())
    else:
        print('fullmatch is not complete.')
main()
