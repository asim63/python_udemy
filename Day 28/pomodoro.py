from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(14)

def reset_timer():
    canvas.itemconfig(timer_text, text = "00:00")
    window.after(1000, countdown, 0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    seconds = count % 60
    minutes = count // 60
    if seconds < 10:
        seconds = f'0{seconds}'
        
    
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0 :
       window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


#TIMER
label = Label(text = "Timer", font =("Courier", 40, "bold "), bg = YELLOW, fg = GREEN )
label.grid(row = 0, column = 1)


#image
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = r"Day 28\tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", font = (FONT_NAME, 35, "bold"), fill = 'white')
canvas.grid(row = 1,column = 1)

#button1
button1 = Button(text = "Start", command = start_timer, highlightthickness = 0)
button1.grid(row = 2,column = 0)
button1.config(padx = 5, pady = 2)

#button1
button2 = Button(text = "Reset", command = reset_timer,  highlightthickness = 0)
button2.grid(row = 2,column = 2)
button2.config(padx = 5, pady = 2)

#checkmark
label2 = Label(text = "✔", font = (FONT_NAME, 14),  bg = YELLOW, fg = GREEN)
label2.grid(row = 3,column = 1)



window.mainloop()