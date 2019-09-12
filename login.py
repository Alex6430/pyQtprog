# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pyodbc
from signup import Ui_signUp
from value import Ui_MainWindow

server = 'DESKTOP-UP524EV'
database = 'new1 диплом'
username = ''
password = ''
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class Ui_Dialog(object):

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        #msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    def valueShow(self):
        self.valueWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.valueWindow)
        self.valueWindow.show()

    def signupShow(self):
        self.signupWindow = QtWidgets.QDialog()
        self.ui = Ui_signUp()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()

    def loginCheck(self):
        username = self.username_edit.text()
        password = self.pass_edit.text()

        result = cursor.execute("select * from auth_user where username = ? and password = ?", (username, password))

        if (len(result.fetchall()) > 0):
            self.valueShow()
            print("User found")
        else:
            print("User no found")
            self.showMessageBox("Ошибка", "Не верный логин или пароль!")

        #cursor.close()
        print("login button click")

    def signUpCheck(self):
        self.signupShow()
        print("signup button click")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 411)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(130, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(130, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.username_edit = QtWidgets.QLineEdit(Dialog)
        self.username_edit.setGeometry(QtCore.QRect(230, 160, 161, 25))
        self.username_edit.setObjectName("username_edit")
        self.pass_edit = QtWidgets.QLineEdit(Dialog)
        self.pass_edit.setGeometry(QtCore.QRect(230, 200, 161, 25))
        self.pass_edit.setObjectName("pass_edit")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(130, 250, 112, 34))
        self.login_btn.setObjectName("login_btn")
        ########### button event
        self.login_btn.clicked.connect(self.loginCheck)
        ############
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(260, 250, 112, 34))
        self.signup_btn.setObjectName("signup_btn")
        ########### button event
        self.signup_btn.clicked.connect(self.signUpCheck)
        ############
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login form"))
        self.u_name_label.setText(_translate("Dialog", "Логин:"))
        self.pass_label.setText(_translate("Dialog", "Пароль:"))
        self.login_btn.setText(_translate("Dialog", "вход"))
        self.signup_btn.setText(_translate("Dialog", "регистрация"))
        self.label.setText(_translate("Dialog", "Авторизация"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
