# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sandbox\same_button_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        #Form.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.QtWindowStaysOnTopHint)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hello"))
        self.pushButton.setText(_translate("Form", "Same Function 1"))
        self.pushButton_2.setText(_translate("Form", "Same Function 2"))
        self.pushButton_3.setText(_translate("Form", "Same Function 3"))