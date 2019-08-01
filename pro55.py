import re
def main():
    s1 = input('Enter a matching string.')
    m = re.match(s1,'Learning python is very easy')
    print(m)
    if m !=None:
        print('Yes it is matched.')
    else:
        print('No it is not matched.')
main()
