from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.mime.application
from email import encoders
import smtplib


def main():

	sender = 'sender email'
	recipient = 'recipient email'

	message = 'Hello world!'

	password = "sender's email password"
	msg = MIMEMultipart('alternative')
	msg['From'] = 'Friend'
	msg['To'] = recipient
	msg['Subject'] = "Examination"

	msg.attach(MIMEText(message, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com: 587')

	server.starttls()
	server.login(sender, password)
	 
	server.sendmail(sender, recipient, msg.as_string())
	 
	server.quit()
	 
	print ("successfully sent email to %s:", (recipient))


if __name__ == '__main__':
	main()