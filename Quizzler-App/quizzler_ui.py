from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # This makes us see the functionalities Quiz Brain class has to offer.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.resizable(width=False, height=False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0/15", bg=THEME_COLOR, fg='white', font=('Ariel', 12, "bold"), anchor=E)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=320, height=260, highlightthickness=0, bg='white')
        self.question = self.canvas.create_text(160, 130, text="", font=('Ariel', 20, "italic"),
                                                fill=THEME_COLOR, width=280)  # width lets the text fit appropriately.

        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=1)

        messagebox.showinfo(title='Welcome!', message="Hey there, Welcome to my Quizzler app!\n\n"
                                                      "This application has been created to test your knowledge of "
                                                      "different topics.\n\n"
                                                      "The questions are generated randomly from a large database"
                                                      " so don't think you can memorize the answers and get away with"
                                                      " it.\n\nGood Luck! [You're gonna need it, hehe]")

        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='Congratulations!\n'
                                                       'You have reached the end of the quiz!')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true(self):
        is_user_right = self.quiz.check_answer('True')
        self.show_feedback(is_user_right)

    def false(self):
        is_user_right = self.quiz.check_answer('False')
        self.show_feedback(is_user_right)

    def show_feedback(self, is_user_right):
        if is_user_right:
            self.canvas.config(bg="green")
            # Configure the score here because it only changes when user is right.
            score = self.quiz.score
            self.score_label.config(text=f"Score: {score}/15")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)
