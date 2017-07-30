# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\Wood_checked.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    number =0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textBrowser_content = QtWidgets.QTextBrowser(Form)
        self.textBrowser_content.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.textBrowser_content.setObjectName("textBrowser")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 51, 20))
        self.label.setObjectName("label")

        self.textBrowser_result = QtWidgets.QTextBrowser(Form)
        self.textBrowser_result.setGeometry(QtCore.QRect(10, 211, 381, 31))
        self.textBrowser_result.setObjectName("textBrowser_content")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 270, 181, 20))
        self.lineEdit.setObjectName("lineEdit")


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 192, 51, 20))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "답 쓰기:"))
        self.label_2.setText(_translate("Form", "정답"))
        self.pushButton.setText(_translate("Form", "다음"))

