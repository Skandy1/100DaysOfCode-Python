import keys as K
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.client=Client(K.account_sid,K.auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=K.TWILIO_NUMBER,
            to=K.MY_NUMBER
        )
        print(message.status)