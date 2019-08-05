from threading import *
import time

class Mythread(Thread):
    def __init__(self,threadID, name, counter):
        Thread.__init__(self)
        #super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('starting ' + self.name)
        print_time(self.name,3,self.counter)

def print_time(threadName,counter,delay):
       print(delay)
       while counter:
            time.sleep(delay)
            print('%s: %s' % (threadName,time.ctime(time.time())))
            counter -=1
thread1 = Mythread(1,'Thread-1',2)
thread1.start()

