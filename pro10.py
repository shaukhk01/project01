import re
def main():
    matched = re.finditer('[^abc]','abcABC')
    count =0
    for m in matched:
        print(m.start(),'--',m.group())
        count +=1
    print('no of occurence.',count)
main()
