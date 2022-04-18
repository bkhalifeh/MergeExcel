from PySide2.QtCore import Signal, QObject


class SignalInt(QObject):
    sig = Signal(int)


class SignalStr(QObject):
    sig = Signal(str)
