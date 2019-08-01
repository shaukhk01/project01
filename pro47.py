import re
def main():
    match = re.finditer('[^abc]','ABCabc')
    for m in match:
        print(m.start(),'---',m.group())
main()
