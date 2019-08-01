import re
def main():
    s1 = re.split(',','Annie,Bridget,Hector')
    print(s1)
    for m in s1:
        print(m)
main()
