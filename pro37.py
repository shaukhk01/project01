import re
def main():
    s1 = input('Enter a identifier.')
    s2 = re.fullmatch('[a-k][0369][a-zA-Z0-9#@]*',s1)

    if s2 !=None:
        print(s1,'valid identifier.')
    else:
        print(s1,'invalid identifier.')
main()
