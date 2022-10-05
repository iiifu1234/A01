import pyvisa
import time
from threading import Thread
from queue import Queue

class VISACMD:
    def open_visa(self):
        rm = pyvisa.ResourceManager()
        rm.close()
        time.sleep(0.01)
        rm = pyvisa.ResourceManager()
        allports=rm.list_resources()
        return rm,allports

    def ask_idn(self,rm,q,port=''):   
        try:
            inst = rm.open_resource(port)
            time.sleep(0.005)
            data = inst.query("*IDN?")
            if 'GW' or 'PSW' in data :
                inst.close()
                q.put((port,data))
                return port,data
            inst.close()
            return 'No Data'
        except pyvisa.errors.VisaIOError:
            # inst.close()
            return "Error: Timeout(request IDN fail)"
        except Exception:
            inst.close()
            return 'Error: None'

    def visa_port_select(self,rm,port='',cmd='*IDN?'):
        inst = rm.open_resource(port)
        inst.write(cmd)
        try:
            data = inst.read()
            return data
        except Exception:
            return

if __name__ == "__main__":
    va = VISACMD()
    rm = va.open_visa()
    q = Queue()
    # a = va.visa_port_select(rm[0],'ASRL3::INSTR','*IDN?')
    # print(a)
    tjobs=[]
    # for i in rm[1]:
    #     data = va.ask_idn(rm[0],q,i)
    #     print(data)

    for i in rm[1]:
        t = Thread(target=va.ask_idn,args=(rm[0],q,i))
        tjobs.append(t)
        t.start()

    for t in tjobs:
        t.join()
    print(q.qsize())
    for i in range(q.qsize()):
        print(q.get())

    rm[0].close()

  