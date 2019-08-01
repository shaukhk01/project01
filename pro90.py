def main():
    class p:
        def __init__(self):
            self.x = 10
    class c(p):
        def __init__(self):
            self.x = 20
            super().__init__()
            print(self.x)
    o = c()
main()            
