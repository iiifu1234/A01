

class PEL2004A:
    def __init__(self) -> None:
        self.endstr = ''
        self.idn = '*IDN?' + self.endstr
        self.rst = '*RST' + self.endstr
        self.read_volt = ';:MEAS:VOLT?' + self.endstr
        self.read_curr = ';:MEAS:CURR?' + self.endstr
        self.read_pow = ';:MEAS:POW?' + self.endstr


    def set_channel(self, ch=1):
        return ';:CHAN ' + str(ch) + self.endstr

    def set_voltage_range(self, vol=16.0):
        return ';:CONF:VOLT:RANG ' + str(vol) + self.endstr

    def set_volt_level(self, vol_l1=5.0):
        return f';:VOLT:L1 {vol_l1}'

    def set_curr_limit(self, volt_curr=2.0):
        return f';:VOLT:CURR {volt_curr}' + self.endstr

    def set_volt_mode(self, mode=0):
        m = 'SLOW' if mode == 0 else 'FAST'
        return f';:VOLT:MODE {m}' + self.endstr

    # def set_mode(self,mode):
    #     if mode == 0:
    #         def set_curr_static_mode(self, ccx=1, curr_l1=5.0, curr_rise=3.2, curr_fall=3.2):
    #             mode = 'CCH' if ccx >= 1 else 'CCL'
    #             curr_rise = curr_rise / 1000
    #             curr_fall = curr_fall / 1000
    #             return f';:MODE {mode};:CURR:STAT:L1 {curr_l1};:CURR:STAT:RISE {curr_rise};:CURR:STAT:FALL {curr_fall}' + self.endstr
    #     else:
    #         def set_curr_dynamic_mode(self, ccdx=1, curr_l1=5.0, curr_l2=0, curr_rise=3.2, curr_fall=3.2, curr_t1=0, curr_t2=0):
    #             mode = 'CCDH' if ccdx >= 1 else 'CCDL'
    #             curr_rise = curr_rise / 1000
    #             curr_fall = curr_fall / 1000
    #             return f';:MODE {mode};:CURR:DYN:L1 {curr_l1};:CURR:DYN:L1 {curr_l2};:CURR:DYN:RISE {curr_rise}' \
    #                    f';:CURR:DYN:FALL {curr_fall};:CURR:DYN:T1 {curr_t1}ms;:CURR:DYN:T2 {curr_t2}mS' + self.endstr

    def set_curr_static_mode(self, ccx=1, curr_l1=5.0, curr_rise=3.2, curr_fall=3.2):
        mode = 'CCH' if ccx >= 1 else 'CCL'
        curr_rise = curr_rise / 1000
        curr_fall = curr_fall / 1000
        return f';:MODE {mode};:CURR:STAT:L1 {curr_l1};:CURR:STAT:RISE {curr_rise};:CURR:STAT:FALL {curr_fall}' + self.endstr

    def set_curr_dynamic_mode(self, ccdx=1, curr_l1=5.0, curr_l2=0, curr_rise=3.2, curr_fall=3.2, curr_t1=0,
                              curr_t2=0):
        mode = 'CCDH' if ccdx >= 1 else 'CCDL'
        curr_rise = curr_rise / 1000
        curr_fall = curr_fall / 1000
        return f';:MODE {mode};:CURR:DYN:L1 {curr_l1};:CURR:DYN:L1 {curr_l2};:CURR:DYN:RISE {curr_rise}' \
               f';:CURR:DYN:FALL {curr_fall};:CURR:DYN:T1 {curr_t1}ms;:CURR:DYN:T2 {curr_t2}mS' + self.endstr

    def set_mode(self, mode):
        return f';:MODE {mode}' + self.endstr


if __name__ == '__main__':
    a = PEL2004A()
    print(a.read_curr)
    # print(a.set_curr_dynamic_mode())
