import time

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import keys as K


class EditMovie(FlaskForm):
    rating = StringField(label='Your rating out of 10? e.g:7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    done = SubmitField(label='Done')


class AddMovie(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    done = SubmitField(label='Search')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class MovieList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.String(250), nullable=True)


db.create_all()


@app.route("/")
def home():
    all_movies = MovieList.query.order_by(MovieList.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking=len(all_movies)-i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    movid = id
    movie = MovieList.query.get(movid)
    new_form = EditMovie()
    if new_form.validate_on_submit():
        movie.rating = new_form.rating.data
        movie.review = new_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=new_form, movname=movie.title)


@app.route('/delete/<int:id>')
def delete_record(id):
    to_delete = MovieList.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add_movie():
    new_add_movie = AddMovie()
    if new_add_movie.validate_on_submit():
        get_string = new_add_movie.title.data
        return redirect(url_for('search', searchkey=get_string))
    return render_template("add.html", form=new_add_movie)


@app.route("/select/<searchkey>")
def search(searchkey):
    make_req = \
        requests.get(url=f"https://api.themoviedb.org/3/search/movie?api_key={K.API_KEY}&query={searchkey}").json()[
            'results']
    movie_id = [x['id'] for x in make_req]
    list_of_movies = [f"{x['original_title']}-{x['release_date']}" for x in make_req]
    return render_template('select.html', list=list_of_movies, ids=movie_id, lenth=len(movie_id))


@app.route("/select/<int:id>")
def selected(id):
    get_details_movie = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}?api_key={K.API_KEY}").json()
    get_title = get_details_movie['title']
    get_year = get_details_movie['release_date'].split('-')[0]
    get_desc = get_details_movie['overview']
    get_image_url = f"https://image.tmdb.org/t/p/w500{get_details_movie['poster_path']}"
    db_id=add_data(get_title, get_desc, get_year, get_image_url)

    return redirect(url_for('edit', id=db_id))


# return redirect(url_for('home'))


def add_data(title, desc, year, img_url):
    new_movie = MovieList(title=title, description=desc, year=year, image_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    time.sleep(1)
    get_id = MovieList.query.filter_by(title=title).first()
    return get_id.id


if __name__ == '__main__':
    app.run(debug=True)
