#!/usr/bin/env python
import csv
import smtplib
import re


from email.mime.text import MIMEText

textfile = 'Text'
fp = open(textfile, 'r')
message_template = fp.read()
fp.close()


server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login('xxx@xxx.com', 'xxx')
email_data = csv.reader(open('Report.csv', 'rb'))
email_pattern = re.compile("^.+@.+\..+$")
for row in email_data:
    if row[3] == '1':
        print "Sending email to {}".format(row[2])
        updated_message = message_template.replace('*', row[0], 1)
        msg = MIMEText(updated_message)
        msg['Subject'] = 'MAUI Field Trial'
        msg['From'] = 'xxx@xxx.com'
        if email_pattern.search(row[2]):
            del msg['To']
            msg['To'] = row[2]
            try:
                server.sendmail('abubnova@quantenna.com', [row[2]], msg.as_string())
            except smtplib.SMTPException as exc:
                print "An error occurred: {}".format(exc)
                break

server.quit()
