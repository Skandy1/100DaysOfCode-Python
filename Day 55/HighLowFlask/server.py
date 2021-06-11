import random

from flask import Flask
actual_number=random.randint(0,9)
print(actual_number)
app=Flask(__name__)
@app.route("/")
def home_page():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif' width=500>"
@app.route("/<int:num>")
def check_number(num):
    if actual_number<num:
        return "<h1 style='color:purple'>Too High!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=400>"
    elif actual_number>num:
        return "<h1 style='color:red'>Too Low!</h1>" \
               "<img src='https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif' width=400>"
    else:
        return "<h1 style='color:green'>You got it right!</h1>" \
               "<img src='https://media.giphy.com/media/3o6Zt8ims21yJLweek/giphy.gif' width=400>"

if __name__=="__main__":
    app.run(debug=True)