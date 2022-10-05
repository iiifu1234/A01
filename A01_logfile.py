import csv

def openfile(filename,data=None,mode='a+',line=None,filemode='normal'):
    file = open(filename,mode,newline=line)
    if filemode.lower() == 'csv':
        writer = csv.writer(file)
        if data:
            writer.writerow(data)
    else:
        if data:
            writefile(file,data)
    file.close()

def writefile(file,data):      
    file.write(data)



if __name__ == "__main__":
    import random

    # for i in range(5):
    #     num = str(round(random.uniform(5.5,10.0),2)) + ','
    #     openfile('log.csv',num)
    # with open("ex2.csv","w",newline='') as csvfile:
    #     writer = csv.writer(csvfile)   
    #先寫入columns_name
        # writer.writerow(["a","b","c","d","message"])   
        # writer.writerows([[1,2,3,4,'hello'],[5,6,7,8,'world'],[9,10,11,12,'foo']])
        # writer.writerow([11,22,33,44,55])
    data = ['測試次數','錯誤次數','讀取電壓']
    openfile('ex1.csv',data,line='',filemode='csv')