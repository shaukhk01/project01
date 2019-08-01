import re
def main():
    s1 = input('Enter a string.')
    s2 = re.search('^learning',s1)
    if s2 !=None:
        print('yes it start ',s2.group())
    else:
        print('no its not start..')
main()
