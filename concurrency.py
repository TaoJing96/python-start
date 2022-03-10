import os
import time
from multiprocessing import Process, Pipe, Lock, set_start_method


def say(word):
    time.sleep(1)
    print('hello ', word, ' pid:', os.getpid())
    print('hello ', word, ' ppid:', os.getppid()) # parent pid
    time.sleep(3)


def sync_say(lock: Lock, word: str):
    lock.acquire()
    try:
        print('hello ', word, ' pid:', os.getpid())
        print('hello ', word, ' ppid:', os.getppid())  # parent pid
    finally:
        lock.release()


if __name__ == '__main__':
    # 启动进程demo
    # p1 = Process(target=say, args=('p1',))
    # p2 = Process(target=say, args=('p2',))
    # p1.start()
    # p2.start()

    # 进程同步
    set_start_method('fork') # 默认是spawn mac只支持fork
    lock = Lock()
    p1 = Process(target=sync_say, args=(lock, 'p1'))
    p2 = Process(target=sync_say, args=(lock, 'p2'))
    p1.start()
    p2.start()