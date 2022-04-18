from design import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from handle import HandleClicked, HandleOther
from merge import Merge
import os


class Window(QMainWindow, Ui_MainWindow, HandleClicked, HandleOther):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.pushButton_merge.clicked.connect(self.onClicked_merge)
        self.pushButton_clearList.clicked.connect(self.onClicked_clearList)
        self.pushButton_selectFiles.clicked.connect(self.onClicked_selectFiles)
        self.mrg = Merge(self.listWidget_excelFiles)
        self.mrg.setOnFinished(self.onFinished_merge)
        self.mrg.setOnReadExcelFile(self.onReadExcelFile)
        self.lastDirectoryOpened = os.getcwd()
