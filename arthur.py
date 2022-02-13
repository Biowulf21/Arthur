# import dependencies
from PyQt5 import QtWidgets, uic
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import sys

# import UI Files
from Arthur import Ui_MainWindow

#import modules
from sendMail import bulkSendMail


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
        subject = self.ui.subjectBodyLineEdit.text()
        print(f'subject is {subject}')
        message = self.ui.templateLineEdit.toPlainText()
        print(f'message is {message}')

        # gets the emails from the receipient text edit and turns it into individual strings
        emails = self.ui.receipientTextEdit.toPlainText()
        receipientList = emails.split()
        print(f'receipient list is  {receipientList}')
        # TODO: Add ability to add attachments
        sentList = []
        # list of emails that were unsuccessfuly sent
        unsentList = []
        attachment = 'james'

        # setting the progress bar
        maxValue = len(receipientList)
        self.ui.progressBar.setMaximum(maxValue)
        print(f'number of recepients are: {maxValue}')

        # set up minimum value for progressbar
        progressValue = 1

        # update progress bar based on the how many receipients have been sent and email already
        for receipient in receipientList:
            self.ui.progressBar.setValue(progressValue)
            # add email to sent list
            sendStatus = bulkSendMail(
                receipient=receipient, subject=subject, emailBody=message, attachment=attachment)
            try:
                if sendStatus == True:
                    sentList.append(receipient)
                elif sendStatus == False:
                    unsentList.append(receipient)
                else:
                    print('Unknown error')
            except Exception as e:
                print(e)
            print(f'unsent list is {unsentList}')
            print(f'sent list is {sentList}')
            progressValue += 1
        self.ui.sentListWidget.addItems(sentList)
        self.ui.failedSentList.addItems(unsentList)
        self.ui.progressBar.setValue(0)
        print('done')


if __name__ == "__main__":
    app = QApplication([])
    win = UI()
    win.setWindowTitle('Arthur - Crusader Email')
    win.show()
    sys.exit(app.exec())
