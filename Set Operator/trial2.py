import asyncio
from aiosmtpd.controller import Controller
import smtplib

class ForwardingHandler:
    def __init__(self, relay_host, relay_port, relay_user, relay_password):
        self.relay_host = relay_host
        self.relay_port = relay_port
        self.relay_user = relay_user
        self.relay_password = relay_password

    async def handle_DATA(self, server, session, envelope):
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        message_data = envelope.content.decode('utf-8', errors='replace')

        print(f"Forwarding email from: {mail_from}")
        print(f"Recipients: {rcpt_tos}")
        print(f"Message data:\n{message_data}")

        # Forward email to Outlook SMTP server
        try:
            with smtplib.SMTP(self.relay_host, self.relay_port) as relay:
                relay.starttls()  # Secure the connection
                relay.login(self.relay_user, self.relay_password)
                relay.sendmail(mail_from, rcpt_tos, envelope.content)
                print("Email forwarded successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Please check your email and app password.")
        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
        except Exception as e:
            print(f"Failed to forward email: {e}")
        return '250 Message forwarded'

async def start_server():
    handler = ForwardingHandler(
        relay_host="smtp.outlook.com",         # Outlook SMTP server
        relay_port=587,                        # SMTP port
        relay_user="nitin.gawande1@outlook.com",  # Your Outlook email
        relay_password="Nitin@1234"   # Your Outlook App Password
    )
    controller = Controller(handler, hostname="127.0.0.1", port=2525)  # Changed port to 2525
    print("SMTP server running on localhost:2525")
    controller.start()
    try:
        await asyncio.Event().wait()  # Keep the server running
    except KeyboardInterrupt:
        print("SMTP server stopped.")
        controller.stop()

if __name__ == "__main__":
    # Start the SMTP server
    asyncio.run(start_server())
