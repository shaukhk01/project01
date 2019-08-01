def main():
    s1 = input('Enter a input.')
    s2 = s1.split()
    out = ''
    o = ''
    i = 0
    for x in s2:
        if i % 2!=0:
            out +=s2[i][::-1]
            i +=1
        else:
            i +=1
            out +=' ',x
    print(out)
main()
