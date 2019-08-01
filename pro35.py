import re
def main():
    s1 = 'LearnInG python is Very Easy'
    s2 = re.search('^learning',s1,re.IGNORECASE)

    if s2 !=None:
        print('yes start with.')
    else:
        print('not start with.')
main()
