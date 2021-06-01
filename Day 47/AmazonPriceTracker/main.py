# IMPORTS
from bs4 import BeautifulSoup
import requests
import smtplib
import keys as K

# PRESET VALUE
PRICE_PRESET = 800.0


# send mail function
def send_mail(todays_price):
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=K.MY_EMAIL, password=K.MY_PASSWORD)
        conn.sendmail(from_addr=K.MY_EMAIL, to_addrs=K.MY_EMAIL,
                      msg=f"Subject:Price Drop Alert\n\n Boya Lavelier mic is now Rs.{todays_price} Buy right now!\n{K.URL}"
                      )


# get page
res = requests.get(url=K.URL, headers=K.headers)
res.raise_for_status()

# creating beautiful soup using the HTML page
soup = BeautifulSoup(res.text, 'html.parser')

# getting product price
get_price = soup.find(name="span", id="priceblock_ourprice").text
price = float(get_price.split()[1])

# compare price
if price <= PRICE_PRESET:
    send_mail(price)
    print("Mail Sent!")
else:
    print("Too costly!")
