# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'value.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from image import Example

class Ui_MainWindow(object):

    def imageShow(self):
        import image

        QWidget.ui = Example(QWidget)
        QWidget.ui.show()


        # app = QtWidgets.QApplication(sys.argv)
        # ex = Example()
        # ex.show_me()
        # ex.show()
        # sys.exit(app.exec_())

    def printCheck(self):
        q = self.q_Edit.text()
        nu = self.nu_Edit.text()
        R = self.R_Edit.text()
        K = self.k_Edit.text()
        M = self.m_Edit.text()

        # if (name == "" or email == "" or username == "" or username == "" or password1 == "" or password2 == ""):
        #     print("no insert")
        # elif (password1 == password2):
        #     # result = cursor.execute("insert into auth_user values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        #     # (password1, datetime.now(), 'False', username, name, '', '', 'False', 'True', datetime.now()))
        #     cursor.execute("{CALL proc_reg(?,?,?)}", (password1, username, name))
        #     print("insert")
        # else:
        #     print("no insert")
        # self.im = Example()

        self.imageShow()
        #self.initUI()
        # cursor.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.help_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.help_comboBox.setGeometry(QtCore.QRect(440, 10, 191, 25))
        self.help_comboBox.setObjectName("help_comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 130, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 360, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.q_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.q_Edit.setGeometry(QtCore.QRect(280, 140, 151, 31))
        self.q_Edit.setObjectName("q_Edit")
        self.nu_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nu_Edit.setGeometry(QtCore.QRect(280, 200, 151, 31))
        self.nu_Edit.setObjectName("nu_Edit")
        self.R_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.R_Edit.setGeometry(QtCore.QRect(280, 250, 151, 31))
        self.R_Edit.setObjectName("R_Edit")
        self.k_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.k_Edit.setGeometry(QtCore.QRect(280, 310, 151, 31))
        self.k_Edit.setObjectName("k_Edit")
        self.m_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.m_Edit.setGeometry(QtCore.QRect(280, 360, 151, 31))
        self.m_Edit.setObjectName("m_Edit")


        self.print_Button = QtWidgets.QPushButton(self.centralwidget)
        self.print_Button.setGeometry(QtCore.QRect(170, 430, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.print_Button.setFont(font)
        self.print_Button.setObjectName("print_Button")

        self.print_Button.clicked.connect(self.printCheck)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите размер силы:"))
        self.label_2.setText(_translate("MainWindow", "Коэфициент Пуассона:"))
        self.label_3.setText(_translate("MainWindow", "Радиус штампа:"))
        self.label_4.setText(_translate("MainWindow", "Размер матрицы по fi:"))
        self.label_5.setText(_translate("MainWindow", "Размер матрицы по r:"))
        self.print_Button.setText(_translate("MainWindow", "Построить график"))
