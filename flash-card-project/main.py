from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/russian_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/russian_words.csv")

key = 0
max_index = data.iloc[-1].name

def pick_word():
    global key, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, max_index)
    value = data._get_value(index, 'Russian')
    canvas.itemconfig(word, text=value, fill="black")
    canvas.itemconfig(label, text='Russian', fill="black")
    key = index
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def delete_word():
    global data, max_index
    data = data.drop(key).reset_index(drop=True)
    data.to_csv("data/russian_words_to_learn.csv", index=False)
    max_index -= 1

    pick_word()

def flip_card():
    value = data._get_value(key, 'English')
    canvas.itemconfig(word, text=value, fill="white")
    canvas.itemconfig(label, text='English', fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


window = Tk()
window.title("Flash card game")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthicknes=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 262, image=card_front_image)
label = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic")) #x,y position of text
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_btn = PhotoImage(file="images/right.png")
right_button = Button(image=right_btn, highlightthickness=0,command=delete_word)
right_button.grid(column=0, row=1)

wrong_btn = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_btn, highlightthickness=0,command=pick_word)
wrong_button.grid(column=1, row=1)

pick_word()


window.mainloop()