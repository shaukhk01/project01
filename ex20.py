import time
class Test:
    def __init__(self):
        print('object initialization.')
    def __del__(self):
        print('fulfilling last wish and performing....')
t1  = Test()
time.sleep(5)
print('End application.')
