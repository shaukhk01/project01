import re
def main():
    s = input('Enter pattern to check.')
    match = re.search(s,'@Hello Annie#Bridget')
    if match !=None:
        print('Matching string is available.')
        print('first ocuurence:',match.start(),'--',match.group())
    else:
        print('Matching string is not available.')
main()
