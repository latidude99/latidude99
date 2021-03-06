import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from main.secrets import *


def send(sender, receiver, subject, text):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = text
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL(MERIDIAN99_SMTP)
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.MAIL_SERVER = MERIDIAN99_SMTP
    s.MAIL_PORT = '465'
    s.MAIL_USE_SSL = True
    s.login(MERIDIAN99_LOGIN, MERIDIAN99_PSWD)
    s.sendmail(MERIDIAN99_LOGIN, LATITUDE99_LOGIN, msg.as_string())
    s.quit()
    print('status email has been sent')