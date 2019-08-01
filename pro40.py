import re
def main():
    f1 = open('input.txt','r')
    f2 = open('output.txt','w')

    for line in f1:
        list = re.findall("[789]\d{9}",line)
        for n in list:
            f2.write(n+'\n')
    print('Extracted all Mobile Number into output.txt')
    f1.close()
    f2.close()

main()
