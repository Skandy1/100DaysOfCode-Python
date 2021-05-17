import requests
from twilio.rest import Client
API_KEY= # Your API_KEY from openweathermap
PHONE_NUMBER=# Your Twilio Phone Number
TO_NUMBER= # Your Phone Number
account_sid= # twilio account sid
auth_token= # twilio auth_token
client=Client(account_sid,auth_token)
parameter={
    "appid":API_KEY,
    "lat":12.920491,
    "lon":77.614298,
    "exclude":"current,daily,minutely"
}

get_req=requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
get_req.raise_for_status()
get_weather_hourly=get_req.json()["hourly"][:12]
for x in get_weather_hourly:
    if x['weather'][0]['id'] < 700:
        message = client.messages \
            .create(
            body="Bring an ☂. It's gonna rain!",
            from_=PHONE_NUMBER,
            to=TO_NUMBER
        )
        print(message.status)
        break
