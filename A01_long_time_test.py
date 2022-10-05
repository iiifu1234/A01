
import A01_PSW8013_cmd, A01_logfile
import time
import random

#init_csv_header_data = ['Item', 'Error', 'read voltage']
file_date = time.strftime("%m%d", time.localtime())
file_name = f'D:/log/{file_date} log.csv'
x, y = [], []

A01_logfile.openfile(file_name, line='', filemode='csv')


while True:
    test_count = 0
    error_count = 0
    init_error = 0

    file = open(file_name, 'r')
    a = file.readlines()
    if len(a) > 1:
        b = a[-1].split(',')
        test_count = int(b[0])
        error_count = int(b[1])

    try:
        PSW = A01_PSW8013_cmd.PSW8013CMD()
        rm = pyvisa.ResourceManager()
        rm.close()
        time.sleep(0.1)
        rm = pyvisa.ResourceManager()
        portlist = rm.list_resources()
        # rm = open_visa()
        inst = rm.open_resource('ASRL3::INSTR')
        data = inst.query(PSW.read_idn())
        print(data)
        if 'PSW' in data:
            break
        time.sleep(2)
    except Exception:
        error_count += 1
        init_error += 1
        print('開啟port錯誤')
        time.sleep(3)

while True:
    try:
        # -- Test loop--
        test_count += 1
        time.sleep(0.1)

        # Step1: 設定隨機電壓: 5.5v ~ 10.0v
        inst.write(PSW.setvoltage(random.uniform(5.5, 10.0)))
        time.sleep(0.1)

        # Step2: 設定隨機電流: 0.5A ~ 1.5A
        inst.write(PSW.setcurr(random.uniform(0.5, 1.5)))
        time.sleep(0.5)

        # Step3: 電源供應器輸出
        inst.write(PSW.setouput('1'))
        time.sleep(2)

        # Step4: 讀取電壓值
        data = inst.query(PSW.actualout('V'))
        data = data.replace('\n', '')
        # x.append(test_count)
        # y.append(float(data))
        # plt.plot(x, y, color='blue')
        # plt.pause(0.01)

        # Step5: 確認讀取電壓值是否有變化，是否有小於5.0，如果有，判定錯誤
        if float(data) < 5.0:
            error_count += 1
        print(f'測試次數:{test_count}, 錯誤次數:{error_count},讀取電壓值:{data}')

        try:
            # Step6: 將訊息寫入csv檔案內
            msg = [test_count, error_count, data]
            A01_logfile.openfile(file_name, msg, line='', filemode='csv')
        except Exception:
            print('檔案寫入失敗')

        # Step7: 電源off
        inst.write(PSW.setouput('0'))
        time.sleep(3)

    except KeyboardInterrupt:
        inst.close()
        rm.close()
        print('程式關閉')

    except Exception:
        error_count += 1
        print('error')
        time.sleep(3)
