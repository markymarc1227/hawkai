from PySide6.QtCore import Signal, QEvent
from PySide6.QtWidgets import QLineEdit

class doubleClickable_QLineEdit(QLineEdit):
    doubleClicked = Signal()

    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonDblClick:
            self.doubleClicked.emit()
        return super().event(event)