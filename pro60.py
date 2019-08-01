import re
def main():
    m = re.subn('[a-z]','#','ABcd123')
    print(m[0])
    print('no of occurences',m[1])
main()
