#! /usr/bin/python3
import sys
import os
import subprocess
from PyQt6 import QtGui, QtWidgets, QtCore
import CustomWidgets
import pprint
import config

from pprint import pprint

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ user interface initialisation """
        ico = QtGui.QIcon("img/logo.png")
        self.setWindowIcon(ico)
        self.setGeometry(50, 50, 500, 300)
        self.centerWindow()
        self.setWindowTitle('Генератор послідовних чисел')

        self.editLayout = CustomWidgets.CustomLayout()
        lblFirstNum = QtWidgets.QLabel('Перший номер:')
        lblCountNum = QtWidgets.QLabel('Кількість номерів:')
        self.editFirstNum = CustomWidgets.CustomLineEdit(config.data['fnum'])
        self.editCountNum = CustomWidgets.CustomLineEdit(config.data['count'])
        self.btnOpenFile = CustomWidgets.CustomButton("Відкрити gen.txt", False)
        self.btnOpenFile.clicked.connect(self.openTxtFile)
        bbox = CustomWidgets.CustomButtonBox(True)
        bbox.accepted.connect(self.generate)
        bbox.rejected.connect(self.close)

        self.editLayout.addWidget(lblFirstNum,          0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.addWidget(lblCountNum,          0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.addWidget(self.editFirstNum,    1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.addWidget(self.editCountNum,    1, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.addWidget(self.btnOpenFile,     2, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.editLayout.addWidget(bbox,                 9, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.editLayout)
        pprint(config.data)

    def generate(self):
        """ when generate button was clicked """
        print("кнопка генерації")
        self.btnOpenFile.setEnabled(True)
        self.btnOpenFile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))

    def openTxtFile(self):
        """ when open gen.txt button was clicked """
        fileObj = open('gen.txt', 'w')
        for i in range(int(config.data['fnum']), int(config.data['fnum']) + int(config.data['count']), 1):
            fileObj.write(str(i) + '\n')
        fileObj.close()
        file_path = "gen.txt"
        if sys.platform == 'win32' or sys.platform == 'win64':
            os.system(f'notepad.exe "{file_path}"')
        else:
            subprocess.run(['xdg-open', file_path])

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