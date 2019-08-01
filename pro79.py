def main():
    class bank:
        def getrofi(self):
            return 10
    class sbi(bank):
        def getrofi(self):
            return 7
    class icici(sbi):
        def getrofi(self):
            return 7.5
    o1 = icici()
    print('ICIC rate of interest.',o1.getrofi()) 
    o2 = sbi()
    print('SBI rate of interest.',o2.getrofi())
    o3 = bank()
    print('Bank rate of interest.',o3.getrofi())
main()
