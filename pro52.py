import re
def main():
    match = re.finditer('.','ab1c2@@@d3f4g5')
    for m in match:

        print(m.start(),'--',m.group())
main()
