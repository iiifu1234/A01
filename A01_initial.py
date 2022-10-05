from A01_visa import VISACMD
from threading import Thread
from queue import Queue

va = VISACMD()
rm = va.open_visa()
q = Queue()


def visa_init():
    tjobs = []
    port_dirt = {}
    for port in rm[1]:
        t = Thread(target=va.ask_idn, args=(rm[0], q, port))
        tjobs.append(t)
        t.start()
    for t in tjobs:
        t.join()
    for i in range(q.qsize()):
        qget = q.get()
        port_dirt[qget[0]] = qget[1]
    return port_dirt


if __name__ == '__main__':
    print(visa_init())
