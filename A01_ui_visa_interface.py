import time

import A01_visa
import UI_PyQt


class UI_VISA_Interface:
    def __init__(self):
        self.visa = A01_visa.VISACMD()

    def goto_open_visa(self):
        rm, ports = self.visa.open_visa()
        return rm, ports

    def goto_query_cmd(self, rm,port,cmd):
        data = self.visa.query_data(rm,port,cmd)
        return data



if __name__ == '__main__':
    v = UI_VISA_Interface()
    rm,ports = v.goto_open_visa()
    print(ports)
    time.sleep(0.05)
    data = v.goto_query_cmd(rm,'ASRL3::INSTR','*IDN?')
    print(data)

