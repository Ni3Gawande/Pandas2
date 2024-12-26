import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from bs4 import BeautifulSoup

# List of recipients
emails = ["nitu.gawande95@gmail.com"]

# Sender's email address
sender = "bluesparrow.paritosh.9@gmail.com"
app_password = "nkarlfskpkmkyfnw"  # Your Gmail app password

# HTML message content
html_content = """  
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <meta name="generator" content="LibreOffice 7.1.2.2 (Linux)"/>
    <meta name="created" content="00:00:00"/>
    <meta name="changed" content="00:00:00"/>
    <title>Miracle Brand</title>
    <style type="text/css">
        @page {
            size: 8.5in 11in;
            margin: 0.79in;
        }
        p {
            margin-bottom: 0.1in;
            line-height: 115%;
            background: transparent;
        }
        pre {
            font-family: "Liberation Mono", monospace;
            font-size: 10pt;
            background: transparent;
        }
        a {
            color: #000080;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .footer {
            font-size: 12px;
            margin-top: 20px;
        }
    </style>
</head>
<body lang="en-US" link="#000080" vlink="#800000" dir="ltr">
    <pre>
        *MIRACLE*

        NO MORE HOT SLEEPING: These NASA-Inspired Sheets Infused With Real Silver Changed My Life

        <strong>These Sheets Are Self-Cleaning And Cooling</strong>

        <a href="https://www.jamrbykn.com/a20f0f31e9474a1ae5cc656ebe7cbeeccf4cdf72-0-2-497c2/xxc1xx/xxc2xx/xxc3xx">SHOW ME A MIRACLE</a>

        Are you tired of washing your sheets just for them to get smelly and dirty again?

        It’s time to say goodbye to sweaty sleepless nights!

        <a href="https://www.jamrbykn.com/a20f0f31e9474a1ae5cc656ebe7cbeeccf4cdf72-0-2-497c2/xxc1xx/xxc2xx/xxc3xx">WHAT DOES A MIRACLE FEEL LIKE?</a>
    </pre>

    <div class="footer">
        To stop receiving messages, please visit <a href="https://www.jamrbykn.com/ua20f0f31e9474a1ae5cc656ebe7cbeeccf4cdf72-0-0-0">here</a>.<br />
        Or mail your request to:<br />
        Miracle Brand PO Box 1701 Piscataway, NJ 08855
    </div>
</body>
</html>
 
"""

# Parse HTML and extract plain text
soup = BeautifulSoup(html_content, "html.parser")
plain_text_content = soup.get_text()
plain_text_content = "\n".join([line.strip() for line in plain_text_content.splitlines() if line.strip()])

# Iterate over each recipient and send the email
for recipient in emails:
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = "YouTube Link"

    # Attach the plain text content
    msg.attach(MIMEText(plain_text_content, 'plain'))

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Attach the image file
    # with open(r"C:\Users\parit\Downloads\Untitled_Export_V1.jpeg", "rb") as f:
    #     image = MIMEImage(f.read())
    #     image.add_header('Content-ID', '<image1>')  # Match 'cid:image1' in the HTML content
    #     msg.attach(image)

    # Sending the email via Gmail's SMTP server
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender, app_password)  # Log in to the SMTP server
            server.sendmail(sender, recipient, msg.as_string())
        print(f"Email sent successfully to {recipient}!")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
