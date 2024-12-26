# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# sender = "bluesparrow.paritosh.9@gmail.com"  # Your Gmail address
# recipient = "paritoshg22@yahoo.com"  # Recipient email address
#
# # The plain text message content that the recipient will see
# plain_text_content = """Hi Pari,
# How are you?
# Sender: Lucifer
# """
#
# # Create the email message
# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = recipient
# msg['Subject'] = "Trial 2"
#
# # Attach the plain text message content (it will appear as plain text for the recipient)
# msg.attach(MIMEText(plain_text_content, 'plain'))
#
# # Sending the email via your local SMTP server (adjust as per your setup)
# with smtplib.SMTP('127.0.0.1', 2531) as server:
#     server.sendmail(sender, recipient, msg.as_string())
#
# print("Email sent successfully!")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

sender = "bluesparrow.paritosh.9@gmail.com"  # Your Gmail address
recipient = "test-rivht9aqx@srv1.mail-tester.com"  # Recipient email address

# HTML message content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message</title>
</head>
<body>
    <div>
        <p>Hi Pari,</p>
        <p>How are you?</p>
        <p>Sender: Lucifer</p>
    </div>
</body>
</html>
"""

# Parse HTML and extract plain text using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
plain_text_content = soup.get_text()

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = "Trial 3"

# Attach the plain text content (without HTML tags)
msg.attach(MIMEText(plain_text_content, 'plain'))

# Sending the email via your local SMTP server (adjust as per your setup)
with smtplib.SMTP('127.0.0.1', 2541) as server:
    server.sendmail(sender, recipient, msg.as_string())

print("Email sent successfully!")
