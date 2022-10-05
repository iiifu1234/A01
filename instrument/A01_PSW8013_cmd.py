

class PSW8013CMD:
    def __init__(self) -> None:
        self.endstr = ''
        self.vol_cmd = ':VOLT '
        self.curr_cmd = ':CURR '
        self.ouput_cmd = ':OUTP '
        self.intalresis_cmd = ':RES '
        self.read_idn = '*IDN?' + self.endstr


    def setvoltage(self,value=5.5):
        return ':VOLT ' + str(value) + self.endstr
    
    def setcurr(self,value):
        return self.curr_cmd + str(value) + self.endstr
    
    def setouput(self,value='0'):
        if value=='1' or value.upper() == 'ON' :
            return self.ouput_cmd + '1' + self.endstr
        elif str(value)=='0' or str(value).upper() =='OFF' :
            return self.ouput_cmd + '0' + self.endstr 

    def setintalresis(self,value):
        return self.intalresis_cmd + str(value) + self.endstr
    
    def setvoltslew(self,rising=0.01,falling=0.01):
        return f':VOLT:SLEW:RIS {rising};FALL {falling}' + self.endstr

    def setcurrslew(self,rising=0.01,falling=0.01):
        return f':CURR:SLEW:RIS {rising};FALL {falling}' + self.endstr

    def setoutputdelayon(self,delaytime):
        return f':OUTP:DEL:ON {delaytime}' + self.endstr

    def setoutputdelayoff(self,delaytime):
        return f':OUTP:DEL:OFF {delaytime}' + self.endstr

    def actualout(self,read='VA'):
        v = ':MEAS:VOLT?'
        a = ':MEAS:CURR?'
        return self.re_fun(v,a,read) 

    def readoutstatus(self):
        return ':OUTP?' + self.endstr

    def readlevel(self,read='VA'):
        v = ':VOLT?'
        a = ':CURR?'
        return self.re_fun(v,a,read)   

    def readovpocp(self,read='VA'):
        v = ':VOLT:PROT?'
        a = ':CURR:PROT?'
        return self.re_fun(v,a,read)

    def re_fun(self,v,a,read):
        read = read.upper()
        m= ';'
        if read == 'V':
            return v + self.endstr
        elif read ==  'A':
            return a + self.endstr
        elif len(read)==2 and (read == 'VA' or 'AV'):
            return v + m + a + self.endstr
        else:
            return False  

if __name__ == '__main__':
    pow_sup = PSW8013CMD()
    print(pow_sup.setvoltage(15))
