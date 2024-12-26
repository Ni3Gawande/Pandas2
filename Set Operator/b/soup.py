from bs4 import BeautifulSoup

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
        <p>How are you, idiot?</p>
        <p>Sender: Lucifer</p>
    </div>
</body>
</html>"""

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the plain text content
plain_text = soup.get_text(separator=" ")

# Print the plain text
print(plain_text)
