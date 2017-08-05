import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import UI
from data_handler import data_handler

class MyWindow(QMainWindow, UI.Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

class handler(MyWindow):
    number=0
    dh = data_handler()

    def __init__(self):
        MyWindow.__init__(self)
        self.textBrowser_content.setText(self.dh.get_content(0))
        self.lineEdit.returnPressed.connect(self.sendResult)
        self.pushButton.clicked.connect(self.pressButton)


    def pressButton(self):
        self.number += 1
        text =self.dh.get_content(self.number)
        if text == '끝입니다.':
            self.number = -1
        self.textBrowser_content.setText(text)
        self.textBrowser_result.clear()

    def sendResult(self):
        if -1 != self.number:
            self.textBrowser_result.setText(self.dh.get_result(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    handler = handler()
    handler.show()
    sys.exit(app.exec_())