import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Message
import smtplib

class CustomMessageHandler:
    async def handle_DATA(self, server, session, envelope):
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        message_data = envelope.content.decode('utf-8', errors='replace')

        print(f"Incoming message from: {mail_from}")
        print(f"Recipients: {rcpt_tos}")
        print(f"Message data:\n{message_data}")
        return '250 Message accepted for delivery'

async def start_server():
    handler = CustomMessageHandler()
    controller = Controller(handler, hostname='127.0.0.1', port=1025)
    print("SMTP server running on localhost:1025")
    controller.start()
    try:
        await asyncio.Event().wait()  # Keeps the event loop running
    except KeyboardInterrupt:
        print("SMTP server stopped.")
        controller.stop()

if __name__ == "__main__":
    # Run the SMTP server in an asyncio loop
    asyncio.run(start_server())

