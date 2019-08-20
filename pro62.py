import re
def main():
    s1 = re.split('\.','www.google.com')
    print(s1)
    for s2 in s1:
        print(s2)
main()
print('-'*50)

def main():
    contact = dict()
    no_emp = int(input('Enter a no of Emp:'))
    while no_emp>0:
        name = input('Enter Emp Name')
        p_No = input('Enter Emp Phone Number')
        email= input('Enter Emp Email.')
        contact[name] = p_No.split()+email.split()
        no_emp -=1
    for data in contact:
        print(data,'\t',contact[data])
main()
