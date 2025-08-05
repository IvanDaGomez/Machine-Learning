import os
from twilio.rest import Client

client = Client()

from_message = "whatsapp:+14155238886"
to_message = "whatsapp:+573024690359"

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_message(message):
    client.messages.create(
        from_=from_message,
        to=to_message,
        body=message
    )
if __name__ == "__main__":
    message = "Hello, this is a test message from Twilio!"
    send_message(message)
    print("Message sent successfully!")