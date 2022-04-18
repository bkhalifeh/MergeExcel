from PySide2.QtWidgets import QMessageBox, QFileDialog
import os


class HandleOther(object):
    def onFinished_merge(self, op: str):
        self.progressBar_result.setValue(100)
        QMessageBox.information(self.centralwidget, 'Info',
                            'Output Excel File :\n%s' % (op), QMessageBox.Ok)
        self.pushButton_merge.setEnabled(True)
        self.pushButton_clearList.setEnabled(True)
        self.pushButton_selectFiles.setEnabled(True)

    def onReadExcelFile(self, p: int):
        self.progressBar_result.setValue(p)


class HandleClicked(object):
    def onClicked_merge(self):
        self.pushButton_merge.setEnabled(False)
        self.pushButton_clearList.setEnabled(False)
        self.pushButton_selectFiles.setEnabled(False)
        if self.listWidget_excelFiles.count() == 0:
            QMessageBox.critical(self.centralwidget, 'Error',
                                 'List Of Files Is Empty', QMessageBox.Ok)
        else:
            op = QFileDialog.getSaveFileName(self.centralwidget, 'Save File As',
                                             self.lastDirectoryOpened, 'Excel files (*.xlsx)')[0]
            if op:
                self.mrg.output = op
                self.mrg.start()

    def onClicked_clearList(self):
        self.progressBar_result.setValue(0)
        self.listWidget_excelFiles.clear()

    def onClicked_selectFiles(self):
        self.progressBar_result.setValue(0)
        f = QFileDialog.getOpenFileNames(self.centralwidget, 'Select Excel Files',
                                     self.lastDirectoryOpened, 'Excel files (*.xlsx)')[0]
        if f:
            self.lastDirectoryOpened = os.path.dirname(f[0])
            for i in f:
                self.listWidget_excelFiles.addItem(i)

