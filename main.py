#! /usr/bin/python3
import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import CustomWidgets

from pprint import pprint

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pr = Project()
        self.setCentralWidget(self.pr)
        self.initUI()

    def initUI(self):
        """ user interface initialisation"""
        ico = QtGui.QIcon("img/logo.png")
        self.setWindowIcon(ico)
        self.setGeometry(50, 50, 600, 300)
        self.centerWindow()
        self.setWindowTitle('Генератор послідовних чисел')
        # self.setMenuBar(self._createMenuBar())


    def centerWindow(self):
        """ centering the main window in the center of the screen """
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def event(self, e) -> QtWidgets.QWidget.event:
        """ hotkey handling """
        if e.type() == QtCore.QEvent.Type.WindowDeactivate:
            self.setWindowOpacity(0.85)
        elif e.type() == QtCore.QEvent.Type.WindowActivate:
            self.setWindowOpacity(1)
        elif e.type() == QtCore.QEvent.Type.KeyPress and e.key() == QtCore.Qt.Key.Key_Escape:
            self.close()
        return QtWidgets.QWidget.event(self, e)

class Project(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.editLayout = QtWidgets.QGridLayout()
        lblFirstNum = QtWidgets.QLabel('Перший номер:')
        lblCountNum = QtWidgets.QLabel('Кількість номерів:')
        editFirstNum = QtWidgets.QLineEdit()
        editCountNum = QtWidgets.QLineEdit()
        btnOpenFile = QtWidgets.QPushButton()
        btnOpenFile.setText("Відкрити gen.txt")
        btnOpenFile.setDisabled(True)
        btnOpenFile.setMaximumWidth(300)
        btnOpenFile.setMinimumSize(200, 34)
        bbox = self.initButtonBox()
        self.editLayout.addWidget(lblFirstNum,  0, 0, 1, 1)
        self.editLayout.addWidget(lblCountNum,  0, 1, 1, 1)
        self.editLayout.addWidget(editFirstNum, 1, 0, 1, 1)
        self.editLayout.addWidget(editCountNum, 1, 1, 1, 1)
        self.editLayout.addWidget(btnOpenFile,  2, 0, 1, 2)
        self.editLayout.addWidget(bbox,         9, 0, 1, 2)

        self.editLayout.setAlignment(lblFirstNum, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.setAlignment(lblCountNum, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.setAlignment(btnOpenFile, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.setAlignment(bbox, QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.nomenclatureTbl = Nomenclature(self.db.getNomenclatureUnits())
        # self.tableLayout.addWidget(self.nomenclatureTbl)
        self.editLayout.setContentsMargins(50, 50, 50, 50)
        self.editLayout.setSpacing(30)
        self.editLayout.setRowStretch(0, 30)
        self.editLayout.setRowStretch(1, 30)
        self.setLayout(self.editLayout)

    def initButtonBox(self):
        """ create widget with "Cancel" and "Save" buttons """
        bbox = CustomWidgets.ButtonBox(True)
        # bbox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText('Генерувати')
        # bbox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText('Вихід')
        # bbox.accepted.connect(self.save)
        # bbox.rejected.connect(self.reject)
        return bbox

    def showAll(self):
        #TODO: showing all nomenclature units...
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    ico = QtGui.QIcon("img/logo.png")
    app.setWindowIcon(ico)
    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())
    window = mainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()