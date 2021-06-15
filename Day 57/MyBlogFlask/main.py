from flask import Flask, render_template
import requests
import keys as K

app = Flask(__name__)
posts=requests.get(url=K.BLOG_URL).json()
@app.route('/')
def home():
    return render_template("index.html", posts=posts)
@app.route('/post/<id>')
def post_page(id):
    get_post=posts[int(id)-1]
    return render_template("post.html", blog=get_post)
if __name__ == "__main__":
    app.run(debug=True)
