import sys
class customer:
    bankname = 'NICBANK'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposite(self,amt):
        self.balance = self.balance + amt
        print('Balance after deposite',self.balance)
    def withdraw(self,amt):
        if amt > self.balance:
            print('insufficent balance')
            sys.exit()
        self.balance = self.balance - amt
        print('After withdraw',self.balance)
print('Welcome to ',customer.bankname)
name = input('Enter your name')
c  = customer(name)
while True:
    print('D-deposite\nW-withdraw\nE-exit')
    opt = input('Enter option.')
    
    if opt == 'D':
        amt = int(input('Enter a amount'))
        c.deposite(amt)
    elif opt =='W':
        amt = int(input('Enter a amount.'))
        c.withdraw(amt)
    else:
        print('Invalid input')
        sys.exit()
