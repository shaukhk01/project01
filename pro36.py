import re
def main():
    s1 = 'Learning python is Very Easy'
    s2 = re.search('easy$',s1,re.IGNORECASE)
    if s2 !=None:
        print('Yes ends with')
    else:
        print('No ends with')
main()

