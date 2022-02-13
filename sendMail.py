import email
import smtplib
from tarfile import RECORDSIZE
from time import sleep
from email.message import EmailMessage


def bulkSendMail(receipient, subject, emailBody, attachment):
    sleep(1)
    sender = "crusaderyearbook@xu.edu.ph"
    password = "uisjoyfegjgudwpp"
    print(f'receipient is  {receipient}`')
    print(f'email message is {emailBody}')
    print(f'subject is {subject}')

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receipient

    message.set_content(emailBody)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(message)
    except Exception as e:
        print(e)
        print('Sending Failed')
        sleep(1)
        return False
    print(f'sent to {receipient}')
    print('Done sending')
    sleep(1)
    return True
