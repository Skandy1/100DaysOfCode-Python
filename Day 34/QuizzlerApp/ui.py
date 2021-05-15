THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


# --------------------------- WINDOW -----------------------------------------#
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzii")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="#FFFFFF")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Hi", font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR)
        self.right_image = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_image, highlightthickness=0, command=self.tick_mark)
        self.right.grid(row=2, column=0)
        self.left_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.left_image, highlightthickness=0, command=self.wrong_mark)
        self.wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Your final score: {self.score}")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")


    def tick_mark(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_mark(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.update_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.score += 1
        self.score_text.config(text=f"Score: {self.score}")
