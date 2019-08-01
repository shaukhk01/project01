import re
def main():
    matched = re.finditer('[^A-Za-z0-9]','Hello%#!*&^)(1234abc@WORLD')
    for m in matched:
        print(m.start(),'--',m.group())
main()
