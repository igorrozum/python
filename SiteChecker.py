#!/usr/bin/env python
# __author__ = 'irozum'

import requests
import time
import smtplib
from requests.exceptions import HTTPError

statCode = 0
msg = ""

# If you want to take the website and interval as input
# website = input("Enter the url you'd want to check: ")
# interval = int(input('Please set the interval: '))

website = 'https://google.com' # your website here
interval = 5


def email_alert():
    sender = 'example@yourdomain.com'  # email account to send alert emails from
    password = 'password'
    recipient = 'you@gmail.com'  # Email acc to receive emails to
    server = smtplib.SMTP('smtp.gmail.com', 587)  # mail server and port
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: " + msg,
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n" + msg)


if __name__ == '__main__':
    while True:
        try:
            statCode = requests.get(website, timeout=2).status_code
        except HTTPError as e:
            msg += 'The HTTP error occurred: ' + e
        except Exception as e:
            msg += 'Some error occurred'
        finally:
            if statCode != 200 and statCode != 400:
                email_alert()
                time.sleep(1800)
        time.sleep(interval)


