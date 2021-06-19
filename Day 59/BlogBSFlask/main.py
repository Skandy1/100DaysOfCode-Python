from flask import Flask, render_template
import requests

get_blogs=requests.get(url="YOUR OWN NPOINT.IO API ").json()


app=Flask(__name__)

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
    return render_template("index.html",blog_list=get_blogs)

@app.route('/post/<id>')
def post_page(id):
    get_post=get_blogs[int(id)-1]
    return render_template("post.html", blog=get_post)

if __name__ == "__main__":
    app.run(debug=True)