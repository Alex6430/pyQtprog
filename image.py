import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication, QComboBox)
from main import printImage
import pyodbc


server = 'DESKTOP-UP524EV'
database = 'new1 диплом'
username = ''
password = ''
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


class value(QWidget):
    def __init__(self):
        super(value, self).__init__()
        self.resize(637, 600)

        self.help_comboBox = QComboBox(self)
        cur = cnxn.cursor()
        res = cur.execute("select is_staff from auth_user where username = ?", (username))
        result = res.fetchone()[0]
        print(result)
        cur.close()

        if result==False:
            self.help_comboBox.addItem("Помощь")
        else:
            self.help_comboBox.addItem("Помощь")
            self.help_comboBox.addItem("Резервная копия БД")
            self.help_comboBox.addItem("Востановить БД")
        # self.help_comboBox.addItems(["Java", "C#", "Python"])
        self.help_comboBox.activated.connect(self.selectionchange)

        self.help_comboBox.setGeometry(QtCore.QRect(440, 10, 191, 25))
        self.help_comboBox.setObjectName("help_comboBox")
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 130, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(50, 360, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.q_Edit = QLineEdit(self)
        self.q_Edit.setGeometry(QtCore.QRect(280, 140, 151, 31))
        self.q_Edit.setObjectName("q_Edit")
        self.nu_Edit = QLineEdit(self)
        self.nu_Edit.setGeometry(QtCore.QRect(280, 200, 151, 31))
        self.nu_Edit.setObjectName("nu_Edit")
        self.R_Edit = QLineEdit(self)
        self.R_Edit.setGeometry(QtCore.QRect(280, 250, 151, 31))
        self.R_Edit.setObjectName("R_Edit")
        self.k_Edit = QLineEdit(self)
        self.k_Edit.setGeometry(QtCore.QRect(280, 310, 151, 31))
        self.k_Edit.setObjectName("k_Edit")
        self.m_Edit = QLineEdit(self)
        self.m_Edit.setGeometry(QtCore.QRect(280, 360, 151, 31))
        self.m_Edit.setObjectName("m_Edit")

        self.print_Button = QPushButton(self)
        self.print_Button.setGeometry(QtCore.QRect(170, 430, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.print_Button.setFont(font)
        self.print_Button.setObjectName("print_Button")

        self.setWindowTitle("value")
        self.label.setText("Введите размер силы:")
        self.label_2.setText("Коэфициент Пуассона:")
        self.label_3.setText("Радиус штампа:")
        self.label_4.setText("Размер матрицы по fi:")
        self.label_5.setText("Размер матрицы по r:")
        self.print_Button.setText("Построить график")

    def selectionchange(self, i):
        # print("Items in the list are :")
        # for count in range(self.help_comboBox.count()):
        #     print(self.help_comboBox.itemText(count))
        # print("Current index", i, "selection changed ", self.help_comboBox.currentText())
        if i == 0:
            print("help")
        elif i == 1:
            self.backup()
            print("1")
        elif i == 2:
            self.restore()
            print("2")

    def backup(self):
        # create a cursor
        connection1 = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                                     server='DESKTOP-UP524EV', database='master',
                                     trusted_connection='yes', autocommit=True)
        backup = '''
                BACKUP DATABASE [new1 диплом] 
            	TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Backup\рез_коп_бд.bak' WITH NOFORMAT, 
            	NOINIT,  
            	NAME = N'new1 диплом-Полная База данных Резервное копирование', 
            	SKIP, 
            	NOREWIND, 
            	NOUNLOAD,  
            	STATS = 10
            	'''
        cursor = connection1.cursor().execute(backup)
        connection1.close()
        print("backup")

    def restore(self):
        # create a cursor
        connection2 = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                                     server='DESKTOP-UP524EV', database='master',
                                     trusted_connection='yes', autocommit=True)

        connection2.cursor().execute("EXEC restor")
        connection2.commit()
        connection2.close()
        print('restore')

    def printCheck(self):
        q = self.q_Edit.text()
        nu = self.nu_Edit.text()
        R = self.R_Edit.text()
        K = self.k_Edit.text()
        M = self.m_Edit.text()
        flag = False

        if (q == "" or nu == "" or R == "" or K == "" or M == ""):
            print("no insert пустые")
            self.showMessageBox("Ошибка", "Заполните пустые строчки")
            flag = False
        else:
            try:
                float(q) and float(nu) and float(R) and float(K) and float(M)
                flag = True
                print('True')
            except:
                print('False')
                self.showMessageBox("Ошибка", "Введите правельные значения")
                flag = False

        if flag==True:
            print("proc do")
            self.procImage(q, nu, R, K, M)
            print("proc after")

    def procImage(self, q, nu, R, K, M):
        qf = float(q)
        nuf = float(nu)
        Rf = float(R)
        Kf = float(K)
        Mf = float(M)
        cur = cnxn.cursor()
        cur.execute("insert into Q(Value_Q) values(?)", qf)
        cur.execute("insert into Nu(Value_Nu) values(?)", nuf)
        cur.execute("insert into R(Value_R) values(?)", Rf)
        cur.execute("insert into MatrixSize(ID_K,ID_M) values(?,?)", (Kf, Mf))
        cur.commit()
        cur.close()
        print("zanos")
        self.w2 = image()
        self.w2.show()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        # msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


class signup(QWidget):
    def __init__(self):
        super(signup, self).__init__()
        self.resize(597, 519)
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(140, 20, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.name_label = QLabel(self)
        self.name_label.setGeometry(QtCore.QRect(250, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.email_label = QLabel(self)
        self.email_label.setGeometry(QtCore.QRect(250, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.username_label = QLabel(self)
        self.username_label.setGeometry(QtCore.QRect(250, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.pass_label = QLabel(self)
        self.pass_label.setGeometry(QtCore.QRect(250, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.password_label = QLabel(self)
        self.password_label.setGeometry(QtCore.QRect(180, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.signup_button = QPushButton(self)
        self.signup_button.setGeometry(QtCore.QRect(200, 450, 191, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signup_button.setFont(font)
        self.signup_button.setObjectName("signup_button")
        ########### button event
        self.signup_button.clicked.connect(self.signUpCheck)
        ############
        self.name_edit = QLineEdit(self)
        self.name_edit.setGeometry(QtCore.QRect(200, 130, 191, 25))
        self.name_edit.setObjectName("name_edit")
        self.email_edit = QLineEdit(self)
        self.email_edit.setGeometry(QtCore.QRect(200, 190, 191, 25))
        self.email_edit.setObjectName("email_edit")
        self.username_edit = QLineEdit(self)
        self.username_edit.setGeometry(QtCore.QRect(200, 250, 191, 25))
        self.username_edit.setObjectName("username_edit")
        self.pass_edit = QLineEdit(self)
        self.pass_edit.setGeometry(QtCore.QRect(200, 320, 191, 25))
        self.pass_edit.setObjectName("pass_edit")
        self.password_edit = QLineEdit(self)
        self.password_edit.setGeometry(QtCore.QRect(202, 400, 191, 25))
        self.password_edit.setObjectName("password_edit")

        self.setWindowTitle("singUp")
        self.label.setText("Регистрация")
        self.name_label.setText("Имя")
        self.email_label.setText("Почта")
        self.username_label.setText("Логин")
        self.pass_label.setText("Пароль")
        self.password_label.setText("Подтверждение пароля")
        self.signup_button.setText("Зарегистрировать")

    def signUpCheck(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        username = self.username_edit.text()
        password1 = self.pass_edit.text()
        password2 = self.password_edit.text()

        if (name == "" or email == "" or username == "" or username == "" or password1 == "" or password2 == ""):
            print("no insert")
            self.showMessageBox("Ошибка", "Заполните поле!")
        elif (password1 == password2):
            cur = cnxn.cursor()
            # result = cursor.execute("insert into auth_user values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            # (password1, datetime.now(), 'False', username, name, '', '', 'False', 'True', datetime.now()))
            cur.execute("{CALL proc_reg(?,?,?)}", (password1, username, name))
            # self.valueShow()
            cur.commit()
            cur.close()
            print("insert")
            self.showMessageBox("", "Вы зарегистрировались!")
        else:
            print("no insert")
            self.showMessageBox("Ошибка", "Введены разные пароли!")

        # cursor.close()

        print("login button click")

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        # msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


class image(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.p = printImage()
        print("srabotala p")
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("graf" + str(self.p) + ".png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(500, 500)
        self.setWindowTitle('График')
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('login')
        self.resize(497, 411)
        self.u_name_label = QLabel(self)
        self.u_name_label.setGeometry(QtCore.QRect(130, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QLabel(self)
        self.pass_label.setGeometry(QtCore.QRect(130, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.username_edit = QLineEdit(self)
        self.username_edit.setGeometry(QtCore.QRect(230, 160, 161, 25))
        self.username_edit.setObjectName("username_edit")
        self.pass_edit = QLineEdit(self)
        self.pass_edit.setGeometry(QtCore.QRect(230, 200, 161, 25))
        self.pass_edit.setObjectName("pass_edit")
        self.login_btn = QPushButton(self)
        self.login_btn.setGeometry(QtCore.QRect(130, 250, 112, 34))
        self.login_btn.setObjectName("login_btn")
        ########### button event
        self.login_btn.clicked.connect(self.loginCheck)
        ############
        self.signup_btn = QPushButton(self)
        self.signup_btn.setGeometry(QtCore.QRect(260, 250, 112, 34))
        self.signup_btn.setObjectName("signup_btn")
        ########### button event
        # self.signup_btn.clicked.connect(self.show_window_1)
        self.signup_btn.clicked.connect(self.show_signup)
        ############
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.u_name_label.setText("Логин:")
        self.pass_label.setText("Пароль:")
        self.login_btn.setText("вход")
        self.signup_btn.setText("регистрация")
        self.label.setText("Авторизация")

    def loginCheck(self):
        global username
        username = self.username_edit.text()
        password = self.pass_edit.text()

        cur = cnxn.cursor()

        result = cur.execute("select * from auth_user where username = ? and password = ?", (username, password))

        if (len(result.fetchall()) > 0):
            self.show_value()
            print("User found")
        else:
            print("User no found")
            self.showMessageBox("Ошибка", "Не верный логин или пароль!")

        # cursor.close()
        cur.close()
        print("login button click")

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        # msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    def show_value(self):
        self.w1 = value()
        self.w1.print_Button.clicked.connect(self.w1.printCheck)
        # self.w1.print_Button.clicked.connect(self.show_image)

        # self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    # def show_image(self):
    #     self.w2 = image()
    #     self.w2.show()

    def show_signup(self):
        self.w3 = signup()
        self.w3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # w.show_signup()
    w.show()
    # w.show_window_1()
    sys.exit(app.exec_())
