from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)

print(answer)
@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="0 to 9 numbers">')


@app.route('/<int:number>')
def logic(number):
    if number < answer:
        return ('<h1 style="color:red">Too Low,try again!!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="slow dog">')
    elif number > answer:
        return ('<h1 style="color:purple">Too High,try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="fast dog">')
    else:
        return ('<h1 style="color:green">Correct Answer!!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="happy dog">')


if __name__ == "__main__":
    app.run(debug=True)
