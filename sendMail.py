import smtplib
from time import sleep


def bulkSendMail(receipient):
    sleep(3)
    print(f'sent to {receipient}')
    print('Done sending')
