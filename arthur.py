# import dependencies
from PyQt5 import QtWidgets, uic
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import sys

# import UI Files
from Arthur import Ui_MainWindow

#import modules
import sendMail


class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Arthur - Crusader Email')
    win.show()
    sys.exit(app.exec())
