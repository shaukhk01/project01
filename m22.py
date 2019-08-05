from threading import *
import time

def main():
    print('current Thread:',current_thread().getName(),'started.....')
    time.sleep(2)
    print('current Thread:',current_thread().getName(),'ended.....')
t1 = Thread(target = main,name = 'ChildThread-1')
t2 = Thread(target = main, name= 'ChildThread-2')
t1.start()
t2.start()

print(t1.name,'isAlive',t1.isAlive())
print(t2.name,'isAlive',t2.isAlive())

print('*' * 10)
time.sleep(2)
print(t1.name,'isAlive',t1.isAlive())
print(t2.name,'isAlive',t1.isAlive())
