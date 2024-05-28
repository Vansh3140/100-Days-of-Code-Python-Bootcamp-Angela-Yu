from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/index.html")
def head():
    response = requests.get(" https://api.npoint.io/674f5423f73deab1e9a7")
    blog_data = response.json()
    return render_template("index.html", blog_datas=blog_data)


@app.route("/About")
def About_page():
    return render_template("about.html")


@app.route("/Contact")
def Contact_page():
    return render_template("contact.html")


@app.route("/<blog_title>")
def post_blog(blog_title):
    blog_subtitle = request.args.get('blog_subtitle')
    blog_body = request.args.get('blog_body')
    print(blog_body)
    return render_template("post.html", Title=blog_title, Subtitle=blog_subtitle, blog_Body=blog_body)


if __name__ == ("__main__"):
    app.run(debug=True)
