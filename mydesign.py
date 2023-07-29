# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\templates\telegramParser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(410, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(410, 190))
        MainWindow.setMaximumSize(QtCore.QSize(410, 190))
        MainWindow.setAcceptDrops(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.linkTelegram = QtWidgets.QLineEdit(self.centralwidget)
        self.linkTelegram.setGeometry(QtCore.QRect(95, 10, 306, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.linkTelegram.setFont(font)
        self.linkTelegram.setText("")
        self.linkTelegram.setObjectName("linkTelegram")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 10, 76, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(15, 55, 106, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_countMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.le_countMessage.setGeometry(QtCore.QRect(130, 55, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_countMessage.setFont(font)
        self.le_countMessage.setText("")
        self.le_countMessage.setObjectName("le_countMessage")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(15, 105, 211, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(15, 145, 211, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 55, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.le_aberageView = QtWidgets.QLineEdit(self.centralwidget)
        self.le_aberageView.setGeometry(QtCore.QRect(240, 105, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_aberageView.setFont(font)
        self.le_aberageView.setText("")
        self.le_aberageView.setPlaceholderText("")
        self.le_aberageView.setObjectName("le_aberageView")
        self.le_countUser = QtWidgets.QLineEdit(self.centralwidget)
        self.le_countUser.setGeometry(QtCore.QRect(240, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_countUser.setFont(font)
        self.le_countUser.setText("")
        self.le_countUser.setPlaceholderText("")
        self.le_countUser.setObjectName("le_countUser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TelegramParser"))
        self.linkTelegram.setPlaceholderText(_translate("MainWindow", "Ссылка на канал по типу - https://t.me/book_sofi"))
        self.label.setText(_translate("MainWindow", "Telegram"))
        self.label_2.setText(_translate("MainWindow", "Кол-во постов"))
        self.le_countMessage.setPlaceholderText(_translate("MainWindow", "Количество постов"))
        self.label_3.setText(_translate("MainWindow", "Среднее кол-во просмотров"))
        self.label_4.setText(_translate("MainWindow", "Количество участников"))
        self.pushButton.setText(_translate("MainWindow", "Считать"))