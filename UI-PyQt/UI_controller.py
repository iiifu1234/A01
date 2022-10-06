
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Clpiass, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def UI_variable_manage(self):
        #-----Button 管理區-----
        self.btn_openFile = self.ui.btn_openfile
        self.btn_selectTest = self.ui.btn_testselect
        self.btn_gotoTest = self.ui.btn_gototest

        #-----list 管理區-----
        self.ls_file_test_item = self.ui.ls_fileTestItem
        self.ls_select_test_item = self.ui.ls_selectTestItem



    def setup_control(self):
        self.UI_variable_manage()      # 與UI變數管理宣告
        self.ls_select_test_item.setVisible(False)
        self.btn_selectTest.setVisible(False)
        # self.ui.pushButton.setVisible(False)
        self.ui.centralwidget.setWindowTitle('List Test')
        self.btn_selectTest.clicked.connect(self.btn_sendto)
        self.btn_openFile.clicked.connect(self.open_file)
        self.test_item()

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