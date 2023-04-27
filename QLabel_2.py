from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel

class clickable_Qlabel(QLabel):
    clicked=Signal(str)

    def mousePressEvent(self, ev):
        self.clicked.emit(ev)