from tkinter import *
import pandas
import random

to_learn={}
current_card={}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_ori=pandas.read_csv("data/german_list.csv")
    to_learn=data_ori.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")



# ---------------------------- NEXT-CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    flip_timer = window.after(3000, flip_card)

# ---------------------------- OPEN FILE ------------------------------- #
def is_known():
    global current_card
    to_learn.remove(current_card)
    data_to_learn=pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- FLIP-CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- GUI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# ---------------------------- CANVAS ------------------------------- #
canvas = Canvas(width=805, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTON ------------------------------- #
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
correct_button = Button(image=tick_image, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

# ---------------------------- MAINLOOP ------------------------------- #
next_card()
window.mainloop()
