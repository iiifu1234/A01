

class ASR3400:
    def __init__(self) -> None:
        self.id = 'ASR'
        self.endstr = ''
        self.read_curr = ';:MEAS:CURR?' + self.endstr
        self.read_output_states = ';:OUTP ?' + self.endstr
        self.read_volt = ';:MEAS:VOLT?' + self.endstr
        self.read_volt_high = ':MEAS:VOLT:HIGH?' + self.endstr
        self.read_volt_low = ':MEAS:VOLT:LOW?' + self.endstr
        self.read_curr = ';:MEAS:CURR?' + self.endstr
        self.read_curr_low = ';:MEAS:CURR:LOW?' + self.endstr
        self.read_curr_high = ';:MEAS:CURR:HIGH?' + self.endstr

    def read_idn(self):
        return '*IDN?' + self.endstr

    def init_ASR3400(self):
        pass

    def set_voltage(self, voltage):
        return ';:VOLT ' + str(voltage) + self.endstr

    def set_voltage_range(self, voltage=100):
        return ';:VOLT:RANG ' + str(voltage) + self.endstr

    def set_output(self, value=0):
        if value == 1:
            return f';:OUTP ON' + self.endstr
        elif value == 0:
            return f';:OUTP OFF' + self.endstr

    def set_frequency(self, freq=60.0):
        return f';:FREQ {freq}'

    def set_mode(self, mode=0):
        if mode == 0:
            m = 'ACDC-INT'
        elif mode == 1:
            m = 'AC-INT'
        elif mode == 2:
            m = 'DC-INT'
        elif mode == 3:
            m = 'ACDC-EXT'
        elif mode == 4:
            m = 'AC-EXT'
        elif mode == 5:
            m = 'ACDC-ADD'
        elif mode == 6:
            m = 'AC-ADD'
        elif mode == 7:
            m = 'ACDC-Sync'
        elif mode == 8:
            m = 'AC-Sync'
        return f';:MODE {m}' + self.endstr


if __name__ == '__main__':
    a  = ASR3400()
    print(a.set_mode(5))