import time
class Test:
    def __init__(self):
        print('constructor excution.')
    def __del__(self):
        print('Destructor excution.')
t1 = Test()
t2 = t1
t3 = t2
del t1
time.sleep(5)
print('object not yet destoryed')
del t2
time.sleep(5)
print('object not yet destoryed')
del t3
time.sleep(5)
print('object deleted..')

