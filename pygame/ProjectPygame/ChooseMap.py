import sys
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QDesktopWidget, QPushButton, QLabel, QMessageBox
from PyQt5.uic.properties import QtGui


class ChooseMap(QWidget):

    def __init__(self):
        super().__init__()
        self.choose()

    def choose(self):
        action, okBtnPressed = QInputDialog.getItem(
            self,
            "Карта",
            "Выберите карту",
            ("Hill", "Mountain", "MonstersHouse"),
            1,
            False
        )
        if okBtnPressed:
            self.map = action + ".txt"
        else:
            self.map = "Hill.txt"
