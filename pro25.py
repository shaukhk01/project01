import re
def main():
    patter = input('Enter a string.')
    matched = re.match(patter,'abcdefgh')
    if matched !=None:
        print('matched is available.')
        print(matched.start(),'--',matched.group())
    else:
        print('match not matched')
main()
