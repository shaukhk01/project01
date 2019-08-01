import re
def main():
    open_data = open('input.txt','r')
    write_data = open('mobile.txt','w')

    for no in open_data:
        list_data = re.findall('[7-9]\d{9}',no)
        for number in list_data:
            write_data.write(number+'\n')
    print('Extracted all mobile number into mobile.txt')
main()
