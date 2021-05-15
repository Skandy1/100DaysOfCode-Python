import requests

para = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
get_req = requests.get(url="https://opentdb.com/api.php", params=para).json()
question_data = get_req['results']
