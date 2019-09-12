# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
from datetime import datetime, date, time

server = 'DESKTOP-UP524EV'
database = 'new1 диплом'
username = ''
password = ''
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class Ui_signUp(object):

    def signUpCheck(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        username = self.username_edit.text()
        password1 = self.pass_edit.text()
        password2 = self.password_edit.text()

        if (name == "" or email == "" or username == "" or username == "" or password1 == "" or password2 == ""):
            print("no insert")
        elif (password1 == password2):
            # result = cursor.execute("insert into auth_user values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            # (password1, datetime.now(), 'False', username, name, '', '', 'False', 'True', datetime.now()))
            cursor.execute("{CALL proc_reg(?,?,?)}", (password1, username, name))
            # self.valueShow()
            print("insert")
        else:
            print("no insert")

        # cursor.close()
        print("login button click")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 519)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(250, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(250, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(250, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(250, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(180, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(200, 450, 191, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_button.setFont(font)
        self.signup_button.setObjectName("signup_button")
        ########### button event
        self.signup_button.clicked.connect(self.signUpCheck)
        ############
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setGeometry(QtCore.QRect(200, 130, 191, 25))
        self.name_edit.setObjectName("name_edit")
        self.email_edit = QtWidgets.QLineEdit(Dialog)
        self.email_edit.setGeometry(QtCore.QRect(200, 190, 191, 25))
        self.email_edit.setObjectName("email_edit")
        self.username_edit = QtWidgets.QLineEdit(Dialog)
        self.username_edit.setGeometry(QtCore.QRect(200, 250, 191, 25))
        self.username_edit.setObjectName("username_edit")
        self.pass_edit = QtWidgets.QLineEdit(Dialog)
        self.pass_edit.setGeometry(QtCore.QRect(200, 320, 191, 25))
        self.pass_edit.setObjectName("pass_edit")
        self.password_edit = QtWidgets.QLineEdit(Dialog)
        self.password_edit.setGeometry(QtCore.QRect(202, 400, 191, 25))
        self.password_edit.setObjectName("password_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("singUp", "Dialog"))
        self.label.setText(_translate("Dialog", "Регистрация"))
        self.name_label.setText(_translate("Dialog", "Имя"))
        self.email_label.setText(_translate("Dialog", "Почта"))
        self.username_label.setText(_translate("Dialog", "Логин"))
        self.pass_label.setText(_translate("Dialog", "Пароль"))
        self.password_label.setText(_translate("Dialog", "Подтверждение пароля"))
        self.signup_button.setText(_translate("Dialog", "Зарегистрировать"))
