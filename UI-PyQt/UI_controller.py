
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):

    def __init__(self):
        # in python3, super(Clpiass, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UI_variable_manage()  # 與UI變數管理宣告
        self.setup_control()
        self.count = 0

    def UI_variable_manage(self):
        #-----Button 管理區-----
        self.btn_openFile = self.ui.btn_openfile
        self.btn_selectTest = self.ui.btn_testselect
        self.btn_gotoTest = self.ui.btn_gototest

        #-----list 管理區-----
        self.ls_file_test_item = self.ui.ls_fileTestItem
        self.ls_select_test_item = self.ui.ls_selectTestItem

        #-----table 管理區-----
        self.testtable = self.ui.testTable

    def setup_control(self):
        self.ls_select_test_item.setVisible(False)
        self.btn_selectTest.setVisible(False)
        # self.ui.pushButton.setVisible(False)
        self.ui.centralwidget.setWindowTitle('List Test')
        self.btn_selectTest.clicked.connect(self.btn_sendto)
        self.btn_openFile.clicked.connect(self.open_file)
        self.btn_gotoTest.clicked.connect(self.goto_test)

        self.test_item()
        self.testtable_init_fun()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(50)
        self.time_counter = 0

    def run(self):
        self.ui.label.setText(str(self.time_counter)) # show time_counter (by format)
        self.time_counter += 1 # time_counter + 1

    def testtable_init_fun(self):
        newItem=QTableWidgetItem('1')
        self.testtable.setItem(0,0,newItem)

        newItem=QTableWidgetItem('Test1')
        self.testtable.setItem(0,1,newItem)

        newItem=QTableWidgetItem('ask idn')
        self.testtable.setItem(0,2,newItem)

        #设置表格头为伸缩模式
        self.testtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 优化3：將表格設置為禁止編輯模式
        self.testtable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #优化4：表格整行选中，表格默认选择的是单个单元格
        self.testtable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 优化5：将行与列的宽度高度与文本内容的宽高相匹配
        QTableWidget.resizeColumnsToContents(self.testtable)
        QTableWidget.resizeRowsToContents(self.testtable)

        # 优化6：表格头的显示与隐藏
        self.testtable.verticalHeader().setVisible(False)
        # self.testtable.horizontalHeader().setVisible(False)

    def goto_test(self):
        # 优化7：在单元格内放置控件
        # ↓放置進度條↓
        style = '''
            QProgressBar {
                border: 2px solid #000;
                border-radius: 5px;
                text-align:center;
                height: 20px;
                width:200px;
            }
            QProgressBar::chunk {
                background: #09c;
                width:1px;
            }
        '''
        # gressbar = QProgressBar()
        # gressbar.setStyleSheet('QProgressBar{margin:3px}')
        # self.testtable.setStyleSheet(style)
        # self.gressbar_select(self.count,3,gressbar)
        # self.count +=1

        # ↓放入文字↓
        label = QLabel()
        self.label_setText(self.count,3,label)

    def label_setText(self,row,col,label):
        label.setText('Wait')
        label.setStyleSheet('color: green')
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.testtable.setCellWidget(row, col, label)
        # self.time_counter <100
        label.setVisible(False)
    def gressbar_select(self,row,col,gressbar):
        self.testtable.setCellWidget(row, col, gressbar)
        max_value = 100
        gressbar.setMaximum(max_value)
        for i in range(max_value):
            gressbar.setValue(i + 1)
            time.sleep(0.01)
    def open_file(self):
        """
        可以直接使用 QFileDialog.getOpenFileName 這個已經設定好的函式，
        直接幫助我們完成開啟檔案的功能，而不同作業系統的問題，在這個功能的底層已經幫我們處理掉了，
        我們可以直接使用。"Open file" 是開始視窗後上方標題列的名稱，
        :return:
        """
        #"./" 代表從哪裡開啟這個目錄，「"./"」就是當前目錄
        filename,filetype= QFileDialog.getOpenFileName(self,"Open file",
                                                         "./",               # start path
                                                         "Txt files(*.txt)") # 限制檔案類型
        if filename:
            self.ls_select_test_item.setVisible(True)
            self.btn_selectTest.setVisible(True)
            f = open(filename)
            for i in f.readlines():
                data = i.split('\n')[0]
                self.ls_file_test_item.addItem(data)

        # self.ui.show_file_path.setText(filename)

    def test_item(self):
        # 開啟一次選擇多個選項
        self.ls_file_test_item.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        # delet=listwidget.takeItem(1)    # 刪除第二個item
        # listwidget2.addItem(delet)      # 添加到listwidget2
        # listwidget.insertItem(0, 'Y')   # 添加純文字項目，加到第0項

        # 添加圖片的方法
        # listwidget.insertItem(0, self.create_item('', 'zcm.jpg'))  # 添加使用函式創造的選項
        # listwidget2.insertItem(0, self.create_item('', 'zcm.jpg'))

        # QListWidget 修改選項
        # item = listwidget.item(3)
        # item.setText('OK')
        # item.setIcon(QtGui.QIcon('zcm.jpg'))

        # listwidget.setFlow(QtWidgets.QListView.LeftToRight)  # 改成水平顯示

        self.ls_file_test_item.doubleClicked.connect(self.showitem)
        self.ls_select_test_item.doubleClicked.connect(self.showitem2)

    def showitem(self):
        text = self.ls_file_test_item.currentItem().text()  # 取得項目文字
        num = self.ls_file_test_item.currentIndex().row()  # 取得項目編號
        self.ls_select_test_item.addItem(text)

    def showitem2(self):
        num = self.ls_select_test_item.currentIndex().row()
        self.ls_select_test_item.takeItem(num)

    def create_item(self,text, img):
        item = QtWidgets.QListWidgetItem()  # 建立清單項目
        item.setText(text)  # 項目文字
        item.setIcon(QtGui.QIcon(img))  # 項目圖片
        return item  # 返回清單項目

    def btn_sendto(self):
        items = self.ls_file_test_item.selectedItems()
        # self.ui.listWidget_2.addItem(items[1].text())
        for i in items:
            self.ls_select_test_item.addItem(i.text())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()

    window.show()
    sys.exit(app.exec_())