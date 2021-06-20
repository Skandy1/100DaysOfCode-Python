from flask import Flask, render_template, request
import requests
import smtplib
import keys as K

get_blogs = requests.get(url="# YOUR NPOINT.IO API LINK").json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", blog_list=get_blogs)


@app.route("/about.html")
def about_page():
    return render_template("about.html")


@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")


@app.route("/index.html")
def index_page():
    return render_template("index.html", blog_list=get_blogs)


@app.route('/post/<id>')
def post_page(id):
    get_post = get_blogs[int(id) - 1]
    return render_template("post.html", blog=get_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    message = request.form['message']
    msg=f"Subject: Feedback from blog\n\n Name: {name}\n Email: {email}\n Phone Number: {number}\n Message: {message}"
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(K.MY_EMAIL, K.MY_PASSWORD)
        conn.sendmail(from_addr=K.MY_EMAIL, to_addrs=K.MY_EMAIL, msg=msg)
    return "<h1>Successfully sent your message!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
