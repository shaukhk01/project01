import re
def main():
    s1 = input('Enter a string.')
    s2 = re.search('easy$',s1)
    if s2 !=None:
        print("Its ends with easy")
    else:
        print("its not ends withs end")
main()
