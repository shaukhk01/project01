import time
class Test:
    def __init__(self):
        print('constructor execution...')
    def __del__(self):
        print('destructor execution..')
list =[Test(),Test(),Test()]
del list
time.sleep(5)
print('End')
