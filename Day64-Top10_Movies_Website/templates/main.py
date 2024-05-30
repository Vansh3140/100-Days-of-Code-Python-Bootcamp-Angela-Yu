from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"

bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    rating_change = FloatField(label='Your rating out of 10 eg:7.5', validators=[DataRequired()])
    review_change = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddMovie(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


# CREATE DB

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE TABLE

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars().all()
    curr_ranking = 1
    for movie in movies:
        movie.ranking = curr_ranking
        db.session.commit()
        curr_ranking += 1
    return render_template("index.html", movies=movies)


@app.route("/edits/<id_>", methods=['GET', 'POST'])
def edit_movie(id_):
    form = MyForm()
    if form.validate_on_submit():
        with app.app_context():
            movie_to_edit = db.session.execute(db.select(Movie).where(Movie.id == int(id_))).scalar()
            movie_to_edit.rating = form.rating_change.data
            movie_to_edit.review = form.review_change.data
            db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form)


@app.route('/<id_>')
def delete_movie(id_):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == int(id_))).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        response = requests.get(url=f"http://www.omdbapi.com/?t={movie_title}&apikey=f69541cb").json()
        with app.app_context():
            new_movie = Movie(
                title=response['Title'],
                year=response['Year'],
                description=response['Plot'],
                img_url=response['Poster'],
                rating=0,
                ranking=0,
                review="nil"
            )
            db.session.add(new_movie)
            db.session.commit()

        with app.app_context():
            latest = db.session.execute(db.select(Movie).where(Movie.title == response['Title'])).scalar()
        return redirect(url_for('edit_movie', id_=latest.id))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
