import re
def main():
    s1 = input('Enter a pattern to check.')
    s2 = re.search(s1,'Hello world learning python')
    if s2 !=None:
        print('Yes it is matched.')
    else:
        print('Yes it is not matched.')
    print('no of occurence',s2.start())
main()
