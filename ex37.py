class outer:
    def __init__(self):
        print('outer class...')
    class inner:
        def __init__(self):
            print('inner class...')
        @staticmethod
        def main():
            print('static method')
o = outer()
o.inner()
o.inner.main()
