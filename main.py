from tkinter import *
import pandas
import random

words = pandas.read_csv("data/spanish_words.csv").to_dict(orient="records")
current_card = {}


def flip_card():
    global current_card
    canvas.itemconfig(lang_name, text="English", fill='white')
    canvas.itemconfig(lang_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card, image=card_back)


# Word generation
def generate_word():
    global current_card, flip_timer
    canvas.itemconfig(card, image=card_front)
    current_card = random.choice(words)
    canvas.itemconfig(lang_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(lang_name, text="Spanish", fill="black")
    flip_timer = window.after(3000, func=flip_card)


# Window config
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)
# Card photo
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
lang_name = canvas.create_text(400, 150, font=("Arial", 40, "italic"), fill="black", text='')
lang_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), fill="black", text='')
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=generate_word)
wrong_button = Button(window, image=wrong_img, borderwidth=0, highlightthickness=0, command=generate_word)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

generate_word()

window.mainloop()
