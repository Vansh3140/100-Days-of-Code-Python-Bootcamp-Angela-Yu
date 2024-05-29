from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    title: Mapped[str] = mapped_column(String(250), primary_key=True, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        data = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = data.scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/add")
def add():
    return render_template('add.html')


@app.post("/")
def add_post():
    book_name = request.form.get('book_name')
    book_author = request.form.get('book_author')
    rating = request.form.get('rating')
    with app.app_context():
        book = Books(title=book_name, author=book_author, rating=rating)
        db.session.add(book)
        db.session.commit()

    with app.app_context():
        data = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = data.scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/change/<book_details>")
def change_rating(book_details):
    with app.app_context():
        data = db.session.execute(db.select(Books).where(Books.title == book_details)).scalar()
        # print(data.title)
    return render_template('rating_change.html', book_details=data)


@app.post('/change/<book_title>')
def final_change_rating(book_title):
    form_data = request.form.get('new_rating')
    with app.app_context():
        data = db.session.execute(db.select(Books).where(Books.title == book_title)).scalar()
        data.rating = float(form_data)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/<book_title>')
def delete(book_title):
    with app.app_context():
        data = db.session.execute(db.select(Books).where(Books.title == book_title)).scalar()
        db.session.delete(data)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
