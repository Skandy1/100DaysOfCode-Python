import requests

import keys as K
from twilio.rest import Client
from smtplib import SMTP


class NotificationManager:
    def __init__(self):
        self.client = Client(K.account_sid, K.auth_token)
        self.get_email = []

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=K.TWILIO_NUMBER,
            to=K.MY_NUMBER
        )
        print(message.status)

    def get_emails(self):
        get_res = requests.get(url="https://api.sheety.co/bbae36cb123714941cad9b23916c12b2/flightDeals/users")
        get_res.raise_for_status()
        for x in get_res.json()['users']:
            self.get_email.append(x['email'])

    def send_emails(self, message, link):
        self.get_emails()
        email_body = f"Subject:Price Drop!\n\n {message} Follow this link to book:{link} "
        with SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=K.MY_EMAIL, password=K.MY_PASSWORD)
            for email in self.get_email:
                conn.sendmail(from_addr=K.MY_EMAIL, to_addrs=email, msg=email_body.encode('utf-8'))
