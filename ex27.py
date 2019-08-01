class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1
    @classmethod
    def main(cls):
        print('no of object is {}'.format(cls.count))
t1 = Test()
t2 = Test()
t1.main()
t3 = Test()
t4 = Test()
t4.main()
