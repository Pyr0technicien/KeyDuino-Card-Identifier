# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(704, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bCreate_user = QtGui.QPushButton(self.centralwidget)
        self.bCreate_user.setGeometry(QtCore.QRect(360, 390, 111, 28))
        self.bCreate_user.setObjectName(_fromUtf8("bCreate_user"))
        self.bValidate_user = QtGui.QPushButton(self.centralwidget)
        self.bValidate_user.setGeometry(QtCore.QRect(220, 390, 101, 28))
        self.bValidate_user.setObjectName(_fromUtf8("bValidate_user"))
        self.user_added = QtGui.QLabel(self.centralwidget)
        self.user_added.setEnabled(False)
        self.user_added.setGeometry(QtCore.QRect(70, 170, 571, 111))
        self.user_added.setObjectName(_fromUtf8("user_added"))
        self.valid_user = QtGui.QLabel(self.centralwidget)
        self.valid_user.setEnabled(False)
        self.valid_user.setGeometry(QtCore.QRect(70, 250, 571, 111))
        self.valid_user.setObjectName(_fromUtf8("valid_user"))
        self.spy_spotted = QtGui.QLabel(self.centralwidget)
        self.spy_spotted.setEnabled(False)
        self.spy_spotted.setGeometry(QtCore.QRect(60, 40, 611, 111))
        self.spy_spotted.setObjectName(_fromUtf8("spy_spotted"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bCreate_user.setText(_translate("MainWindow", "Create user", None))
        self.bValidate_user.setText(_translate("MainWindow", "Validate user", None))
        self.user_added.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">USER ADDED</span></p></body></html>", None))
        self.valid_user.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">VALID USER</span></p></body></html>", None))
        self.spy_spotted.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#ff0000;\">SPY SPOTTED</span></p></body></html>", None))

