import pyvisa
import time
from threading import Thread
from queue import Queue

# rm = pyvisa.ResourceManager()
# rm.close()
# time.sleep(0.01)
# rm = pyvisa.ResourceManager()
# allports = rm.list_resources()


class VISACMD:
    def open_visa(self):
        rm = pyvisa.ResourceManager()
        rm.close()
        time.sleep(0.01)
        rm = pyvisa.ResourceManager()
        ports = rm.list_resources()
        return rm, ports

    def ask_idn(self, rm, q, port=''):
        try:
            inst = rm.open_resource(port)
            time.sleep(0.005)
            data = inst.query("*IDN?")
            if 'GW' or 'PSW' in data:
                inst.close()
                q.put((port, data))
                return port, data
            inst.close()
            return 'No Data'
        except pyvisa.errors.VisaIOError:
            # inst.close()
            return "Error: Timeout(request IDN fail)"
        except Exception:
            inst.close()
            return 'Error: None'

    def query_data(self, rm, port='', cmd='*IDN?'):
        inst = rm.open_resource(port)
        try:
            data = inst.query(cmd)
            return  data
        except Exception:
            return  False



if __name__ == "__main__":
    pass
    va = VISACMD()
    rm = va.open_visa()
    q = Queue()
    tjobs = []
    for i in rm[1]:
        t = Thread(target=va.ask_idn, args=(rm[0], q, i))
        tjobs.append(t)
        t.start()
    for t in tjobs:
        t.join()
    for i in range(q.qsize()):
        print(q.get())

    rm[0].close()
