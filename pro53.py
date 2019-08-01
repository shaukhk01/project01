import re
def main():
    match = re.finditer('a{3,4}','aabccaaadeaeaaaaaacdefa')
    for m in match:
        print(m.start(),'---',m.group())
main()
