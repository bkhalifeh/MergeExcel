from PySide2.QtWidgets import QApplication
from window import Window

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
