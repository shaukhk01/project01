from threading import *
import time

def main():
    for i in range(5):
        print('Annie')
        time.sleep(1)
t1 = Thread(target = main)
t1.start()
t1.join()
for x in range(5):
    print('Hector')
