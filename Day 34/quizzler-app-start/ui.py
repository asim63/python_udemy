from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20 , pady = 20, bg = THEME_COLOR)
        
        TICK = PhotoImage(file =r"Day 34\quizzler-app-start\images\true.png")
        CROSS = PhotoImage(file =r"Day 34\quizzler-app-start\images\false.png")

        #text
        self.my_label = Label(text= f"Score: {self.quiz.score}",fg= 'white', bg= THEME_COLOR)
        self.my_label.grid(column = 1, row = 0)
        #image
        self.canvas = Canvas(width = 300, height = 250, bg = 'white')
        self.question_text = self.canvas.create_text(
            150,
            130,
            width = 280,
            text = "something",
            font = ("Arial", 20, "italic"),
            fill = THEME_COLOR
            )
        self.canvas.grid( column = 0,row = 1, columnspan=2,pady = 50) 
        
        #button
        self.button1 = Button(image = TICK, bg = THEME_COLOR, highlightthickness= 0, command= self.check_true)
        self.button1.grid(column = 0,row = 2)
        
        self.button2 = Button(image = CROSS, bg = THEME_COLOR, highlightthickness= 0, command = self.check_false)
        self.button2.grid(column = 1,row = 2)
        
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = 'white')
        self.my_label.config(text = f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz")
            self.button1.config(state = "disabled")
            self.button2.config(state = "disabled")
            
    def check_true(self):
        user_answer = 'True'
        self.give_feedback(self.quiz.check_answer(user_answer))
        
    def check_false(self):
        user_answer = 'False'
        self.give_feedback(self.quiz.check_answer(user_answer))
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.get_next_question)
        
  
        
            