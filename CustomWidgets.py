import sys
from PyQt6 import QtGui, QtWidgets, QtCore

class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, text):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setText(text)

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, text, enabled=True):
        super().__init__()
        self.setText(text)
        self.setEnabled(enabled)
        self.setMaximumWidth(300)
        self.setMinimumSize(200, 34)

class ButtonBox(QtWidgets.QDialogButtonBox):
    def __init__(self, doubleBtnMode):
        super().__init__()
        if(doubleBtnMode):
            self.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close |
                                QtWidgets.QDialogButtonBox.StandardButton.Ok)
            self.button(QtWidgets.QDialogButtonBox.StandardButton.Close).setObjectName('dlgBtn')
            self.button(QtWidgets.QDialogButtonBox.StandardButton.Close).setText('Вихід')
        else:
            self.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setObjectName('dlgBtn')
        self.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText('Генерувати')
        if sys.platform == 'win32' or sys.platform == 'win64':
            self.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        else:
            self.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))

class DialogGrid(QtWidgets.QGridLayout):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(30, 30, 30, 30)
        self.setSpacing(20)