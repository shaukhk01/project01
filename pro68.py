import re
def main():
    f1 = open('number.txt','r')
    f2 = open('no_list.txt','w')

    for data in f1:
        list = re.findall('[7-9]\d{9}',data)
        for number in list:
            print(number)
        for no in list:
            f2.write(no+'\n')
    print('mobile number extracted successfully....')
main()


