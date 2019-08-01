import re
def main():
    s1 = input('Enter a starting string.')
    s2 = re.search('^learning',s1)

    if s2 !=None:
        print('Yes starting string is',s1)
    else:
        print('Not it start with',s1)
main()
