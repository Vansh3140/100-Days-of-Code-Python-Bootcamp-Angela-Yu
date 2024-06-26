from flask import Flask, render_template, request
import requests
from smtplib import SMTP

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.post('/contact')
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    USERNAME = "chdvanshsingh@gmail.com"
    PASSWORD = "ijav mlod yxuq qsql"

    driver = SMTP('smtp.gmail.com', 587)
    driver.starttls()
    driver.login(user=USERNAME, password=PASSWORD)

    subject = f'{name} has entered details'
    body = f'Name:{name}\n Email:{email}\n Phone:{phone}\n Message:{message}'

    driver.sendmail(from_addr=USERNAME, to_addrs="workman3140@gmail.com", msg=f"Subject:{subject} \n\n {body}")
    driver.close()

    return render_template("contact.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
