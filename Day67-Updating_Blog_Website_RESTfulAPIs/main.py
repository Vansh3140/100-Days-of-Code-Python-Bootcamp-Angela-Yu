from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class Form(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    name = StringField(label='Your Name', validators=[DataRequired()])
    blog_url = URLField(label='Blog Image URL', validators=[DataRequired()])
    blog_content = CKEditorField(label='Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='SUBMIT POST')


@app.route('/')
def get_all_posts():
    posts = []
    with app.app_context():
        all_data = db.session.execute(db.select(BlogPost)).scalars().all()
        for x in all_data:
            posts.append(x)
    return render_template("index.html", all_posts=posts)


@app.route('/posts/<post_id>')
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_post():
    form = Form()
    today = date.today()
    if form.validate_on_submit():
        new_blog = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.name.data,
            img_url=form.blog_url.data,
            body=form.blog_content.data,
            date=f"{today.strftime("%B")} {today.day},{today.year}"
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, token="add")


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_posts(post_id):
    blog_data = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = Form(
        title=blog_data.title,
        subtitle=blog_data.subtitle,
        name=blog_data.author,
        blog_url=blog_data.img_url,
        blog_content=blog_data.body
    )
    today = date.today()
    if form.validate_on_submit():
        blog_data.title = form.title.data
        blog_data.subtitle = form.subtitle.data
        blog_data.author = form.name.data
        blog_data.img_url = form.blog_url.data
        blog_data.body = form.blog_content.data
        db.session.commit()
        return redirect(url_for('show_post',post_id=blog_data.id))
    return render_template('make-post.html', form=form, token="edit")


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>',methods=['GET','DELETE'])
def delete_post(post_id):
    curr_blog = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    db.session.delete(curr_blog)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
