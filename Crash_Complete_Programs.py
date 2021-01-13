# -*- coding: utf-8 -*-
"""
Spyder Editor

Author = Tallal
Task = Get Email/SMS sent
"""
import smtplib
import datetime
from io import StringIO
import logging


def send_email_completion_notification(PASSWORD):
    timestam = datetime.datetime.now() 
    print('connecting')
    try:
        #Note that the server may change based on the email address you use.
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        print('connected')
        email = 'SENDER EMAIL ADDRESS'
        type(smtpObj)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(email, PASSWORD)
        smtpObj.sendmail(email, 'RECIEVING EMAIL ADDRESS',
        'Subject: Python Completed {}.\n Completed Processing at'.format(timestam))
        smtpObj.quit()
        
        print("Completion Email sent to " +  email)
        
        return True
    except:
        print("Can't send Completion Email")
        
def send_email_crash_notification(PASSWORD, MESSAGE):
    timestam = datetime.datetime.now() 
    print('connecting')
    try:
        #Note that the server may change based on the email address you use.
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        print('connected')
        email = 'tallal-usman@outlook.com'
        type(smtpObj)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(email, PASSWORD)
        smtpObj.sendmail(email, 'RECIEVING EMAIL ADDRESS',
        'Subject: Python Crash {}.\n Crashed at {}'.format(timestam, MESSAGE))
        smtpObj.quit()
        
        print("Crash Email sent to " +  email)
        
        return True
    except:
        print("Can't send Crash Email")
        
            
if (__name__ == '__main__'):
    print("Please enter password: ")
    PASSWORD = input()
    
    try:
        #Your main code will be placed here
        print(1+string)
        send_email_completion_notification(PASSWORD)
    except Exception:
        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)
        logging.error("Exception occurred", exc_info=True)
        send_email_crash_notification(PASSWORD, log_stream)
        
        
    try:
        #Your main code will be placed here
        print(1+1)
        send_email_completion_notification(PASSWORD)
    except Exception:
        log_stream = StringIO()
        logging.basicConfig(stream=log_stream, level=logging.INFO)
        logging.error("Exception occurred", exc_info=True)
        send_email_crash_notification(PASSWORD, log_stream)