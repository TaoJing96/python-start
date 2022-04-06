import os
import random
import time
from multiprocessing import Process


def download(url):
    print('download %s start, pid:%s' % (url, os.getpid()))
    time.sleep(random.randint(1, 3))
    print('download %s end, pid:%s' % (url, os.getpid()))


def main():
    p1 = Process(target=download, args=('www.a.png', ))
    p1.start()
    p2 = Process(target=download, args=('www.b.png',))
    p2.start()


if __name__ == '__main__':
    main()