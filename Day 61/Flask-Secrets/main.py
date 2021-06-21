from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email, length

class MyForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email(message="Please enter a correct Email")])
    password=PasswordField('Password', validators=[DataRequired(), length(min=8, message="Password must be minimum "
                                                                                         "8 characters")])
    submit=SubmitField(label='Log In')


app = Flask(__name__)
Bootstrap(app)
app.secret_key="XkaeEkavOap1(aa^"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login_page():
    login_form=MyForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data=="admin@email.com" and login_form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

