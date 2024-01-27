from tkinter import *
import json

# Window config
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# Card photo
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, font=("Arial", 40, "italic"), fill="black", text='Title')
canvas.create_text(400, 263, font=("Arial", 60, "bold"), fill="black", text='Word')
canvas.grid(column=0, row=0, columnspan=2)

# Word generation


# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, borderwidth=0, highlightthickness=0)
wrong_button = Button(window, image=wrong_img, borderwidth=0, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()
