from tkinter import *
import pandas
from random import randint

# Window config
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Card photo
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, font=("Arial", 40, "italic"), fill="black", text='Spanish')
foreign_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), fill="black", text='Word')
canvas.grid(column=0, row=0, columnspan=2)

# Word generation

words = pandas.read_csv("data/spanish_words.csv").to_dict(orient="records")


def generate_word():
    word = words[randint(0, len(words) - 1)]["Spanish"]
    canvas.itemconfig(foreign_word, text=word)


# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=generate_word)
wrong_button = Button(window, image=wrong_img, borderwidth=0, highlightthickness=0, command=generate_word)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()
