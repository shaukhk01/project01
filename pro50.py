import re
def main():
    match = re.finditer('[a-zA-Z0-9]','a2@b1ABc')
    for m in match:
        print(m.start(),'--',m.group())
main()
