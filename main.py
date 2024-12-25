import random
from tkinter import *
from pandas import *
BACKGROUND_COLOR = "#B1DDC6"
words = read_csv("data/french_words.csv")
words_dict = words.to_dict(orient="records")
current_card = {}


def change_cards():

    card.config(file="images/card_back.png")
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=current_card["English"])


def change_words():
    global current_card, flip_timer
    card.config(file="images/card_front.png")
    screen.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(lang, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    flip_timer = canvas.after(3000, func=change_cards)


screen = Tk()
screen.title("Flash Card Project")
screen.config(width=500, height=500, padx=50, pady=50, bg=BACKGROUND_COLOR)


img_true = PhotoImage(file="images/right.png")
button_true = Button(image=img_true, highlightthickness=0, command=change_words)
button_true.grid(row=1, column=0)


img_false = PhotoImage(file="images/wrong.png")
button_false = Button(image=img_false, highlightthickness=0, command=change_words)
button_false.grid(row=1, column=1)


canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)


card = PhotoImage(file="images/card_front.png")
Image = canvas.create_image(400, 270, image=card)


lang = canvas.create_text(400, 100, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 280, text="Word", font=("Ariel", 60, "bold"))

flip_timer = canvas.after(3000, func=change_cards)
change_words()
screen.mainloop()
