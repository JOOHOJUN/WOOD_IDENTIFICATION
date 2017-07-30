import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import UI
from data_handler import dataList

class MyWindow(QMainWindow, UI.Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)



class handler(MyWindow):

    def __init__(self):
        MyWindow.__init__(self)
        self.textBrowser_content.setText(dataList.content[0])
        self.lineEdit.returnPressed.connect(self.sendResult)
        self.pushButton.clicked.connect(self.pressButton)

    def pressButton(self):
        self.number += 1
        if len(dataList.content) != self.number:
            self.textBrowser_content.setText(dataList.content[self.number])
        else:
            self.number = -1
            self.textBrowser_content.setText('끝입니다.')
        self.textBrowser_result.clear()

    def sendResult(self):
        if -1 != self.number:
            self.textBrowser_result.setText(dataList.result[self.number])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    handler = handler()
    handler.show()
    sys.exit(app.exec_())