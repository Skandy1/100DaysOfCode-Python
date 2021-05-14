import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL= # YOUR EMAIL ID
MY_PASSWORD= # YOUR PASSWORD
MY_LAT =  # Your latitude
MY_LONG =  # Your longitude

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if is_night() and is_overhead():
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(MY_EMAIL,MY_PASSWORD)
            conn.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:ISS Passing By!\n\n Hey Skandy, run to your "
                                                                   f"balcony and look up for the ISS satellite ")
