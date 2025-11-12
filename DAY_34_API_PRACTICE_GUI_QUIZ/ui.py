from tkinter import *

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, question):
        self.question = question
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="C:/Users/37529/PycharmProjects/100_days/DAY_34_API_PRACTICE_GUI_QUIZ/images/true.png")
        self.false_image = PhotoImage(file="C:/Users/37529/PycharmProjects/100_days/DAY_34_API_PRACTICE_GUI_QUIZ/images/false.png")

        self.question_text = self.canvas.create_text(140, 130, text=self.question, fill="black", font=("Arial", 15, "italic"))

        self.score = Label(text=f"Score: 0", fg="white", font=("Arial", 12, "italic"), background=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.true_btn = Button(image=self.true_image)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=self.false_image)
        self.false_btn.grid(column=1, row=2)


        self.window.mainloop()

