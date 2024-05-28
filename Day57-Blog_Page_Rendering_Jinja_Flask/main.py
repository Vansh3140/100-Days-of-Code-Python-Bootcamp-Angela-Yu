from flask import Flask, render_template, request
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = response.json()
    return render_template("index.html", blog_data=blog_data)


@app.route('/blogs/<title_blog>')
def send_post(title_blog):
    body_blog = request.args.get('body_blog')
    data = Post(title_blog, body_blog)
    return render_template("post.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
