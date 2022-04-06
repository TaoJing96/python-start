import time
from os import getpid
from multiprocessing import Queue, Process


# queue 进程间通信
def send(queue: Queue):
    while True:
        queue.put('msg')
        print('send success, pid:%s' % getpid())
        time.sleep(1)

def recv(queue: Queue):
    while True:
        msg = queue.get()
        print('recv success, msg:%s, pid:%s' % (msg, getpid()))


def main():
    q = Queue(maxsize=3)
    p1 = Process(target=send, args=(q, ))
    p1.start()
    p2 = Process(target=recv, args=(q,))
    p2.start()


if __name__ == '__main__':
    main()