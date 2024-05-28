from flask import Flask,render_template
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def head():
    curr_year = dt.datetime.now().year
    return render_template("index.html", year=curr_year)

@app.route("/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io/?name={name.capitalize()}")
    age_response = requests.get(f"https://api.agify.io/?name={name.capitalize()}")
    gender = gender_response.json()['gender']
    age = age_response.json()['age']
    return (f"<h1>Hey {name.capitalize()},</h1>"
            f"<h2>I think you are a {gender},</h2>"
            f"<h3>And maybe {age} years old.</h3>")

@app.route("/blog")
def get_blog():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = blog_response.json()
    return render_template("blog.html", blog_data=blog_data)

if __name__=="__main__":
    app.run(debug=True)

