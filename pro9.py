import re
def main():
    matched = re.finditer('[abc]','abcAbckh')
    print(matched)
    for m in matched:
        print(m.start(),'--',m.group())
main()
