##################### Normal Starting Project ######################
import smtplib

import pandas
import datetime as dt
import random

MY_EMAIL = # your mail id
MY_PASSWORD = # your password

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month
today = (today_month, today_day)

birthday_list = pandas.read_csv("birthdays.csv").to_dict('records')

birthdays_dict = {(xyz['month'], xyz['day']): f"{xyz['name']},{xyz['email']},{xyz['year']},{xyz['month']},{xyz['day']}"
                  for xyz in birthday_list}

randi = random.randint(1, 3)
if today in birthdays_dict:
    actual_bdy = birthdays_dict[today]
    name_bdy = actual_bdy.split(",")[0]
    email_bdy = actual_bdy.split(",")[1]
    with open(f"letter_templates/letter_{randi}.txt") as lett:
        read_letter = lett.read()
        update = read_letter.replace("[NAME]", name_bdy)
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.sendmail(from_addr=MY_EMAIL, to_addrs=email_bdy, msg=f"Subject:Happy Birthday!\n\n {update}")
else:
    print("No Birthdays Today!!")
