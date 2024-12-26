import smtplib

sender = "nitin.gawande1@outlook.com"
recipient = "paritoshgonnade@gmail.com"
message = """Subject: Test Email

Pagi is this you

"""

# Use the correct port (2525) for the local SMTP server
with smtplib.SMTP('127.0.0.1', 2526) as server:
    server.sendmail(sender, recipient, message)

print("Email sent successfully!")
