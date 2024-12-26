import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

sender = "bluesparrow.paritosh.9@gmail.com"  # Your Gmail address
recipient = "paritoshgonnade@gmail.com"  # Recipient email address

# HTML message content (with HTML tags and clickable link)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div>
        <p>Hi Pari,</p>
        <p>How are you?</p>
        <p>Sender: Lucifer</p>
        <p><a href="https://google.com/"><img src="https://i.ibb.co/RhcmJCm/Untitled-Export-V1.jpg" alt="Untitled-Export-V1" border="0"></a></p>
    </div>
</body>
</html>
"""

# Parse HTML and extract plain text using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
plain_text_content = soup.get_text()

# Clean up the plain text to remove extra spaces or blank lines
plain_text_content = "\n".join([line.strip() for line in plain_text_content.splitlines() if line.strip()])

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = "Trial 7"

# Attach the HTML content (as HTML) and the plain text version
msg.attach(MIMEText(html_content, 'html'))  # Send the HTML content
msg.attach(MIMEText(plain_text_content, 'plain'))  # Send the plain text content

# Sending the email via your local SMTP server (adjust as per your setup)
with smtplib.SMTP('127.0.0.1', 2531) as server:
    server.sendmail(sender, recipient, msg.as_string())

print("Email sent successfully!")
