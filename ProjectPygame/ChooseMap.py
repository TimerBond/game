import sys
from PyQt5.QtWidgets import QWidget, QInputDialog


class ChooseMap(QWidget):

    def __init__(self):
        super().__init__()
        self.map = "Hill.txt"

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
