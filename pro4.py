def main():
    s1 = input('Enter a input.')
    list_data = []
    for x in s1:
        if x not in list_data:
            list_data.append(x)
        else:
            pass
    print(' '.join(list_data))
main()


