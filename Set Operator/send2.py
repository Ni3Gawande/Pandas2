import smtplib

# Sender and recipient details
sender = "bluesparrow.paritosh.9@gmail.com"
recipient = "paritoshgonnade@gmail.com"
message = """Subject: Test Email

Pagi, is this you?
"""

# Send email using the local SMTP server (localhost on port 1025)
with smtplib.SMTP('127.0.0.1', 1028) as server:
    server.sendmail(sender, recipient, message)

print("Email sent successfully!")