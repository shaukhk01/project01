import re
def main():
   matched = re.finditer('\W','He@llo world12')
   for m in matched:
        print(m.start(),'--',m.group())
main()
