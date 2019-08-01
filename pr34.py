import re
def main():
    s1 = 'Learning python is very easy.'
    s = re.search('easy.$',s1)
    if s !=None:
        print('end with [easy.] string' )
    else:
        print('no ends with given')
main()

