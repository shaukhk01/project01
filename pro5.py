def main():
    s1 = input('Enter a input.')
    output = ''
    for x in s1:
        if x not in output:
            output +=x
            print(x,(str(s1.count(x))))
        else:
            pass
main()
