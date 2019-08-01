def main():
    s1 = input('Enter a input.')
    output = ''
    for x in s1:
        if x.isalpha():
            output +=x
            prev = x
        else:
            output +=chr(ord(prev)+int(x))
    print(output)
main()
