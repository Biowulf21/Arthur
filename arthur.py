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

        # declaring UI elements

        # declaring buttons
        self.ui.sendMailBtn.clicked.connect(self.sendMail)

        self.ui.progressBar.setValue(0)

    def sendMail(self):
        receipientList = []
        # gets the emails from the receipient text edit and turns it into individual strings
        emails = self.ui.receipientTextEdit.toPlainText()
        receipientList = emails.split()

        # list of emails that are successfuly sent
        sentList = []
        # list of emails that were unsuccessfuly sent
        unsentList = []

        # setting the progress bar
        maxValue = len(receipientList)
        self.ui.progressBar.setMaximum(maxValue)
        print(f'number of recepients are: {maxValue}')

        # set up minimum value for progressbar
        progressValue = 1

        for recepient in receipientList:
            # update progress bar based on the how many receipients have been sent and email already
            sendMail.bulkSendMail(recepient)
            self.ui.progressBar.setValue(progressValue)
            progressValue += 1
            # add email to sent list
            sentList.append(recepient)


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Arthur - Crusader Email')
    win.show()
    sys.exit(app.exec())
