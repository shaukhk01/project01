from sys import argv
print('no of command line argv:',len(argv))
print()
print('command line argument  :',argv)
argv = argv[1:]
sum = 0
for x in argv:
    sum += int(x)
    print(x)
print(sum)

