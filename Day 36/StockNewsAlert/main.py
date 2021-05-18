import math

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = # YOUR API_KEY
API_KEY_NEWS = # YOUR API_KEY
MY_NUMBER = # YOUR PHONE NUMBER
TWILIO_NUMBER =# YOUR TWILIO NUMBER
account_sid = # YOUR TWILIO ACCOUNT SID
auth_token = # YOUR TWILIO AUTH TOKEN
client = Client(account_sid, auth_token)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PARAMETERS = {
    "apikey": API_KEY_STOCK,
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY"
}
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "apikey": API_KEY_NEWS
}
req = requests.get(url=STOCK_ENDPOINT, params=PARAMETERS)
req.raise_for_status()
get_json = req.json()
get_daily = get_json['Time Series (Daily)']
data_list = [value for (key, value) in get_daily.items()]
yesterday_closing_price = float(data_list[0]['4. close'])
daybefore_yesterday_closing_price = float(data_list[1]['4. close'])
diff_amount = yesterday_closing_price - daybefore_yesterday_closing_price
up_down = None
if diff_amount > 0:
    up_down = "🔼"
else:
    up_down = "🔽"
diff_percentage = math.ceil((diff_amount / yesterday_closing_price) * 100)
if diff_percentage > 5 or diff_percentage < 5:
    get_news = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    get_articles = get_news.json()['articles'][:3]
    headline_list = [get_articles[x]['title'] for x in range(len(get_articles))]
    for x in headline_list:
        message = client.messages.create(
            body=f"TSLA {up_down}{diff_percentage}\nHeadline:{x}",
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.status)
