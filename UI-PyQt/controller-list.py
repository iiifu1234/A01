
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

    def setup_control(self):
        self.ui.listWidget_2.setVisible(False)
        self.ui.pushButton.setVisible(False)
        self.ui.centralwidget.setWindowTitle('List Test')
        self.ui.pushButton.clicked.connect(self.btn_sendto)
        self.ui.file_button.clicked.connect(self.open_file)

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
        listwidget = self.ui.listWidget
        if filename:
            self.ui.listWidget_2.setVisible(True)
            self.ui.pushButton.setVisible(True)
            f = open(filename)
            for i in f.readlines():
                data = i.split('\n')[0]
                listwidget.addItem(data)


        # self.ui.show_file_path.setText(filename)

    def test_item(self):
        listwidget = self.ui.listWidget
        listwidget2 = self.ui.listWidget_2

        # 開啟一次選擇多個選項
        listwidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
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

        listwidget.doubleClicked.connect(self.showitem)
        listwidget2.doubleClicked.connect(self.showitem2)

    def showitem(self):
        text = self.ui.listWidget.currentItem().text()  # 取得項目文字
        num = self.ui.listWidget.currentIndex().row()  # 取得項目編號
        self.ui.listWidget_2.addItem(text)

    def showitem2(self):
        num = self.ui.listWidget_2.currentIndex().row()
        self.ui.listWidget_2.takeItem(num)

    def create_item(self,text, img):
        item = QtWidgets.QListWidgetItem()  # 建立清單項目
        item.setText(text)  # 項目文字
        item.setIcon(QtGui.QIcon(img))  # 項目圖片
        return item  # 返回清單項目

    def btn_sendto(self):
        items = self.ui.listWidget.selectedItems()
        # self.ui.listWidget_2.addItem(items[1].text())
        for i in items:
            self.ui.listWidget_2.addItem(i.text())





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()

    window.show()
    sys.exit(app.exec_())