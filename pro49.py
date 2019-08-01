import re
def main():
    match = re.finditer('[0-9]','He12llo3@')
    for m in match:
        print(m.start(),'--',m.group())
main()
