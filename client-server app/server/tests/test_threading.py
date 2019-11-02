"""
import threading
import time


def clock(interval):
    while True:
        print('Time now is %s' % time.ctime())
        time.sleep(interval)


if __name__ == '__main__':
    while True:
        p = threading.Thread(target=clock, args=(15, ))
        print('Starting new thread')
        p.start()
        time.sleep(5)
"""
