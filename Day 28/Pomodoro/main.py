from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer", fg=GREEN)
    label_tick.config(text="")
    REPS=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_break)
    elif REPS % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += "✔"
        label_tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50)
window.config(bg=YELLOW)
window.title("Pomodoro")

# labels
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
label.grid(row=0, column=1)

# button start
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# button reset
reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=2)

# tick mark
label_tick = Label(fg=GREEN, font=(FONT_NAME, 16), bg=YELLOW)
label_tick.grid(row=3, column=1)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)
window.mainloop()
