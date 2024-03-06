from tkinter import *

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, q_list):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.curr_score = 0
        self.question_number = 0
        self.question_list = q_list

        self.score = Label(text=f"Score : {self.curr_score}", font=("Sans-Serif", 10, "bold"), fg="white",
                           bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.question = Label(text=f"{self.question_list[self.question_number].text}", pady=10, padx=10,
                              font=("Sans-Serif", 20, "bold"),
                              fg=THEME_COLOR)
        self.question.grid(column=0, row=1, columnspan=2, pady=10)

        self.wrong_image = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\GUI_Quiz_App\\images\\false.png")
        self.wrong_button = Button(image=self.wrong_image, bg=THEME_COLOR, command=self.check_false)
        self.wrong_button.grid(column=0, row=2)

        self.right_image = PhotoImage(file="C:\\Users\\DELL\\PycharmProjects\\GUI_Quiz_App\\images\\true.png")
        self.right_button = Button(image=self.right_image, bg=THEME_COLOR, command=self.check_true)
        self.right_button.grid(column=1, row=2)

        self.window.mainloop()

    def check_true(self):
        if self.still_has_questions():
            answer = self.question_list[self.question_number].answer
            if answer == "True":
                self.update_score()
            self.update_question()

    def check_false(self):
        if self.still_has_questions():
            answer = self.question_list[self.question_number].answer
            if answer == "False":
                self.update_score()
            self.update_question()

    def update_score(self):
        self.curr_score += 1
        self.score.config(text=f"Score : {self.curr_score}")

    def update_question(self):
        self.question_number += 1
        if self.question_number >= 10:
            self.question.config(text=f"Thanks For Playing your Final Score is {self.curr_score}/10")
        else:
            self.question.config(text=f"{self.question_list[self.question_number].text}")

    def still_has_questions(self):
        return self.question_number < 10
