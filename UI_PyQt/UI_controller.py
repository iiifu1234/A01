import time
from A01_ui_visa_interface import UI_VISA_Interface as ui_visa
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

        # MainWindow Title
        self.setWindowTitle('QICON Test')
        # title 旁的ICON
        self.setWindowIcon(QtGui.QIcon('image/gwinstek_logo.ico'))
        # self.resize(490, 660)


        # StatusBar
        self.statusBar().showMessage('GW TestStand!!!')
        self.UI_variable_manage()  # UI變數管理宣告
        self.setup_control()

    def UI_variable_manage(self):
        # -----Button area-----
        self.btn_openFile = self.ui.btn_openfile
        self.btn_openFile.setText('')
        self.btn_openFile.setIcon(QtGui.QIcon('image/blue-folder-horizontal-open.png'))
        # self.btn_openFile.setIcon(self.style().standardIcon(getattr(QStyle, i)))
        self.btn_openFile.setIconSize(QtCore.QSize(64, 64))
        # self.btn_openFile.setText('File')

        # self.btn_selectTest = self.ui.btn_testselect

        self.btn_gotoTest = self.ui.btn_gototest

        # -----list area-----
        self.ls_detail = self.ui.listWidget
        self.ls_file_test_item = self.ui.ls_fileTestItem
        self.ls_select_test_item = self.ui.ls_selectTestItem

        # print(self.wtable.rowCount())
        # -----table area-----
        self.wtable = self.ui.testTable

        # -----Label area------
        self.test_label = self.ui.label
        self.test_label.setVisible(False)

        # -----variable 管理區---
        self.test_dict = {}

    def setup_control(self):
        self.ls_select_test_item.setVisible(False)
        self.btn_openFile.clicked.connect(self.open_file)
        self.btn_gotoTest.clicked.connect(self.goto_test)
        self.wtable.itemDoubleClicked.connect(self.delete_test_item)
        self.test_item()
        self.testtable_init_fun()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(1)
        self._1ms_time_counter = 0
        self._100ms_timer = 0
        self._200ms_timer = 0
        self.testcount = 0

    def run(self):
        # self.ui.label.setText(str(self._200ms_timer))  # show time_counter (by format)
        if self._1ms_time_counter % 200 == 0:
            self._200ms_timer += 1

        if self._1ms_time_counter % 100 == 0:
            self._100ms_timer += 1
        self._1ms_time_counter += 1  # time_counter + 1
        self.text_blinking((self.testcount, 3))
        self.ui.label.setText(str(self.testcount))

    def testtable_init_fun(self):
        # newItem = QTableWidgetItem('1')
        # self.testtable.setItem(0, 0, newItem)
        #
        # newItem = QTableWidgetItem('Test1')
        # self.testtable.setItem(0, 1, newItem)
        #
        # newItem = QTableWidgetItem('ask idn')
        # self.testtable.setItem(0, 2, newItem)

        # 设置表格头为伸缩模式
        self.wtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 优化3：將表格設置為禁止編輯模式
        self.wtable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 优化4：表格整行选中，表格默认选择的是单个单元格
        self.wtable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 优化5：将行与列的宽度高度与文本内容的宽高相匹配
        QTableWidget.resizeColumnsToContents(self.wtable)
        QTableWidget.resizeRowsToContents(self.wtable)

        # 优化6：表格头的显示与隐藏
        self.wtable.verticalHeader().setVisible(False)

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
        # self.testtable.horizontalHeader().setVisible(False)
        # gressbar = QProgressBar()
        # gressbar.setStyleSheet('QProgressBar{margin:3px}')
        # self.wtable.setStyleSheet(style)
        # self.gressbar_select(self.count,3,gressbar)
        # self.count +=1
        # ↓放入文字↓
        # label = QLabel()
        # label.setText('Wait')
        # self.label_setText(self.count, 3, label)
        # label.hide()

    def text_blinking(self, location):
        # read_text = self.wtable.currentItem().text()  # 讀取table指定位置的值
        color = QtGui.QColor(0, 100, 30)
        if self._100ms_timer % 10 == 5:
            self.set_fontcolor(self.wtable, 'Wait', location[0], location[1], color)
        elif self._100ms_timer % 10 == 0:
            self.set_fontcolor(self.wtable, '', location[0], location[1], color)

    def goto_test(self):
        v = ui_visa()
        rm,ports = v.goto_open_visa()
        data = v.goto_query_cmd(rm,'ASRL3::INSTR','*IDN?')
        print(data)

    def label_setText(self, row, col, label):
        label.setStyleSheet('color: green')
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.wtable.setCellWidget(row, col, label)

    def gressbar_select(self, row, col, gressbar):
        self.wtable.setCellWidget(row, col, gressbar)
        max_value = 100
        gressbar.setMaximum(max_value)
        for i in range(max_value):
            gressbar.setValue(i + 1)
            time.sleep(0.01)

    def set_fontcolor(self, table, text, row, col, color):
        newItem = QTableWidgetItem(text)
        newItem.setForeground(color)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # newItem.setForeground(QtGui.QBrush(QtGui.QColor(color)))
        table.setItem(row, col, newItem)

    def open_file(self):
        """
        可以直接使用 QFileDialog.getOpenFileName 這個已經設定好的函式，
        直接幫助我們完成開啟檔案的功能，而不同作業系統的問題，在這個功能的底層已經幫我們處理掉了，
        我們可以直接使用。"Open file" 是開始視窗後上方標題列的名稱，
        :return:
        """
        # "./" 代表從哪裡開啟這個目錄，「"./"」就是當前目錄
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file",
                                                         "./",  # start path
                                                         "Txt files(*.txt)")  # 限制檔案類型
        if filename:
            init = True
            self.ls_select_test_item.setVisible(True)
            self.ls_file_test_item.clear()
            f = open(filename)
            for i in f.readlines():
                keys = i.split('\n')[0].split(',')[0].upper()
                self.test_dict[keys] = []
                if init:
                    item = QListWidgetItem(keys)
                    self.ls_file_test_item.addItem(item)
                    self.ls_file_test_item.setCurrentItem(item)
                    init = False
                else:
                    item = QListWidgetItem(keys)
                    self.ls_file_test_item.addItem(item)
                self.add_test_item(keys)

                for j in i.split('\n')[0].split(','):
                    data = j.strip()
                    if data != keys:
                        self.test_dict[keys].append(data.upper())
            rows = self.wtable.rowCount()
            for i in range(rows):
                color = QtGui.QColor(0, 100, 30)
                self.set_fontcolor(self.wtable, 'Wait', i, 3, color)
            self.ls_text = self.ls_file_test_item.currentItem().text()
            self.show_test_detail()

    def test_item(self):
        # 開啟一次選擇多個選項
        self.ls_file_test_item.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        # delet=listwidget.takeItem(1)    # 刪除第二個item
        # listwidget2.addItem(delet)      # 添加到listwidget2
        # listwidget.insertItem(0, 'Y')   # 添加純文字項目，加到第0項
        # ---
        # 添加圖片的方法
        # listwidget.insertItem(0, self.create_item('', 'zcm.jpg'))  # 添加使用函式創造的選項
        # listwidget2.insertItem(0, self.create_item('', 'zcm.jpg'))
        # ---
        # QListWidget 修改選項
        # item = listwidget.item(3)
        # item.setText('OK')
        # item.setIcon(QtGui.QIcon('zcm.jpg'))
        # listwidget.setFlow(QtWidgets.QListView.LeftToRight)  # 改成水平顯示

        self.ls_file_test_item.doubleClicked.connect(self.show_file_test_item)
        self.ls_file_test_item.clicked.connect(self.show_test_detail)
        # self.ls_select_test_item.doubleClicked.connect(self.showitem2)

    def show_test_detail(self):
        self.ls_text = self.ls_file_test_item.currentItem().text()  # 取得項目文字
        self.ls_select_test_item.clear()
        for i in self.test_dict:
            if self.ls_text == i:
                num = 1
                for detail in self.test_dict[i]:
                    self.add_list_item(self.ls_select_test_item, f'{num}. {detail}')
                    num += 1

    def show_file_test_item(self):
        text = self.ls_file_test_item.currentItem().text()  # 取得項目文字
        num = self.ls_file_test_item.currentIndex().row()  # 取得項目編號
        self.add_test_item(text)

    def delete_test_item(self, Item=None):
        # 如果单元格对象为空
        if Item is None:
            return
        else:
            row = Item.row()  # 获取行数
            col = Item.column()  # 获取列数 注意是column而不是col哦
            text = Item.text()  # 获取内容
            self.wtable.removeRow(row)
            re_num = self.wtable.rowCount()

            for i in range(re_num):
                newItem = QTableWidgetItem(str(i + 1))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)  # 設置字體在中間|字體靠下
                self.wtable.setItem(i, 0, newItem)

    def showitem2(self):
        num = self.ls_select_test_item.currentIndex().row()
        self.ls_select_test_item.takeItem(num)

    def add_test_item(self, text=''):
        row = self.wtable.rowCount()
        self.wtable.setRowCount(row + 1)
        newItem = QTableWidgetItem(str(row + 1))
        newItem.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)  # 設置字體在中間|字體靠下
        self.wtable.setItem(row, 0, newItem)
        newItem = QTableWidgetItem(text)
        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
        self.wtable.setItem(row, 1, newItem)

    def create_item(self, text, img):
        item = QtWidgets.QListWidgetItem()  # 建立清單項目
        item.setText(text)  # 項目文字
        item.setIcon(QtGui.QIcon(img))  # 項目圖片
        return item  # 返回清單項目

    def add_list_item(self, qlist, text):
        item = QListWidgetItem(text)
        qlist.addItem(item)

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
