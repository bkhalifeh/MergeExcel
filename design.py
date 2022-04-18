# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 291)
        icon = QIcon()
        icon.addFile(u"Excel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget_excelFiles = QListWidget(self.centralwidget)
        self.listWidget_excelFiles.setObjectName(u"listWidget_excelFiles")
        self.listWidget_excelFiles.setGeometry(QRect(10, 10, 361, 241))
        self.pushButton_selectFiles = QPushButton(self.centralwidget)
        self.pushButton_selectFiles.setObjectName(u"pushButton_selectFiles")
        self.pushButton_selectFiles.setGeometry(QRect(380, 20, 85, 26))
        self.pushButton_clearList = QPushButton(self.centralwidget)
        self.pushButton_clearList.setObjectName(u"pushButton_clearList")
        self.pushButton_clearList.setGeometry(QRect(380, 50, 85, 26))
        self.pushButton_merge = QPushButton(self.centralwidget)
        self.pushButton_merge.setObjectName(u"pushButton_merge")
        self.pushButton_merge.setGeometry(QRect(380, 80, 85, 26))
        self.progressBar_result = QProgressBar(self.centralwidget)
        self.progressBar_result.setObjectName(u"progressBar_result")
        self.progressBar_result.setGeometry(QRect(10, 260, 361, 23))
        self.progressBar_result.setValue(0)
        self.progressBar_result.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Merge Excel", None))
        self.pushButton_selectFiles.setText(QCoreApplication.translate("MainWindow", u"Select Files", None))
        self.pushButton_clearList.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.pushButton_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
    # retranslateUi

