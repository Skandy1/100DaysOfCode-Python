import requests
import datetime
import keys as K

exer_body = {
    "query": input("What exercise did you do today?"),
    "gender": "male",
    "weight_kg": 55.5,
    "height_cm": 181.5,
    "age": 23
}
exer_header = {
    "x-app-id": K.APP_ID,
    "x-app-key": K.API_KEY
}

res = requests.post(url=K.NUTRIONIX_EXERCISE_ENDPOINT, headers=exer_header, json=exer_body)
res.raise_for_status()
exercise = res.json()['exercises'][0]['name'].title()
duration = res.json()['exercises'][0]['duration_min']
calories = res.json()['exercises'][0]['nf_calories']
date = datetime.datetime.now().date()
formatted_date = date.strftime("%d/%m/%Y")

time = datetime.datetime.now().time()
formatted_time = time.strftime("%H:%M:%S")

row_data = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_header = {
    "Authorization": K.SHEETY_AUTH
}

add_row = requests.post(url=K.SHEETY_ENDPOINT, json=row_data, headers=sheety_header)
add_row.raise_for_status()
print(add_row.text)
