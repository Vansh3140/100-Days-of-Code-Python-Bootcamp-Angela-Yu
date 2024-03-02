from tkinter import *
import pandas as pd
import random

start_1 = 0
x = 0
pair = {"trouve": "find"}
BACKGROUND_COLOR = "#B1DDC6"

# Data

data = pd.read_csv("C:\\Users\\DELL\\PycharmProjects\\Flash_Cards\\data\\french_words.csv")

data_list = [{row.French: row.English} for (index, row) in data.iterrows()]


# Functions

def remove_word():
    global pair
    global start_1
    pair = random.choice(data_list)
    canvas.itemconfig(word, text=list(pair.keys())[0], fill="black")
    canvas.itemconfig(canvas_image, image=img1)
    canvas.itemconfig(canvas_text, text="French", fill="black")
    start1 = window.after(3000, swap)
    for y in data_list:
        if y == pair:
            data_list.remove(y)

    final_list = [{"French": list(y.keys())[0], "English": y[list(y.keys())[0]]} for y in data_list]

    df = pd.DataFrame(final_list)
    df.to_csv("words_to_learn.csv")


def change_word():
    global pair
    global start_1
    pair = random.choice(data_list)
    canvas.itemconfig(word, text=list(pair.keys())[0], fill="black")
    canvas.itemconfig(canvas_image, image=img1)
    canvas.itemconfig(canvas_text, text="French", fill="black")
    start1 = window.after(3000, swap)


def swap():
    global pair
    global start_1
    canvas.itemconfig(canvas_image, image=img2)
    canvas.itemconfig(canvas_text, text="English", fill="white")
    canvas.itemconfig(word, text=pair[list(pair.keys())[0]], fill="white")
    window.after_cancel(start_1)


# UI Of The App

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=65, bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=450, bg=BACKGROUND_COLOR, highlightthickness=0)
img1 = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\Flash_Cards\\images\\card_front.png")
img2 = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\Flash_Cards\\images\\card_back.png")
canvas_image = canvas.create_image(400, 225, image=img1)
canvas_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, padx=20, pady=20)

if x == 0:
    start_1 = window.after(3000, swap)
    x -= 1

# Red Button

cross = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\Flash_Cards\\images\\wrong.png")
red_btn = Button(image=cross, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)
red_btn.grid(column=0, row=1)

# Red Button

right = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\Flash_Cards\\images\\right.png")
green_btn = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word)
green_btn.grid(column=1, row=1)

window.mainloop()
