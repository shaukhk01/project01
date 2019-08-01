def main():
    data = input('enter a string.')
    i = 0
    l = len(data)
    for x in data:
        print(x,i,data[-l],l)
        i +=1
        l -=1
main()
