import re
def main():
    match = re.finditer('[^a-zA-Z0-9]','AbcDEF@#%')
    for m in match:
        print(m.start(),m.group())
main()
