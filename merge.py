from PySide2.QtCore import QThread
from PySide2.QtWidgets import QListWidget
from signals import SignalInt, SignalStr
import xlrd
import xlsxwriter
import win32com.client as win32
import pythoncom


class Merge(QThread):
    def __init__(self, qlw: QListWidget):
        QThread.__init__(self, None)
        self.qlw = qlw
        self.output = None
        self.onFinished = SignalStr()
        self.onReadExcelFile = SignalInt()
        self.oi = 0
        pythoncom.CoInitialize()
        xl = win32.Dispatch('Excel.Application')
        self.xl_id = pythoncom.CoMarshalInterThreadInterfaceInStream(pythoncom.IID_IDispatch, xl)

    def setOnReadExcelFile(self, func):
        self.onReadExcelFile.sig.connect(func)

    def setOnFinished(self, func):
        self.onFinished.sig.connect(func)

    def readFile(self, outw, fp, sr=0):
        wb = xlrd.open_workbook(fp)
        sheet = wb.sheet_by_index(0)
        for i in range(sr, sheet.nrows):
            oj = 0
            for j in range(0, sheet.ncols):
                outw.write(self.oi, oj, sheet.cell_value(i, j))
                oj += 1
            self.oi += 1

    def run(self) -> None:
        self.onReadExcelFile.sig.emit(0)
        self.oi = 0
        workbook = xlsxwriter.Workbook(self.output)
        worksheet = workbook.add_worksheet('info')
        self.readFile(worksheet, self.qlw.item(0).text())
        for i in range(1, self.qlw.count()):
            self.readFile(worksheet, self.qlw.item(i).text(), 1)
            self.onReadExcelFile.sig.emit(i * 100 / self.qlw.count())
        workbook.close()
        xl = win32.Dispatch(pythoncom.CoGetInterfaceAndReleaseStream(self.xl_id, pythoncom.IID_IDispatch))
        wb = xl.Workbooks.Open(self.output)
        for ws in wb.Sheets:
            ws.Columns.AutoFit()
        wb.Save()
        self.onFinished.sig.emit(self.output)
