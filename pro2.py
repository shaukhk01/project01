def main():
    s1 = input('Enter a string.')
    output = ''
    for x in s1:
        if x.isalpha():
            output +=x
            prev = x
        else:
            output +=prev *(int(x)-1)
    print(output)
main()
