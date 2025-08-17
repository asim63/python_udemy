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
reps =0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        countdown(long_break_sec)
        label.config(text = "BREAK", fg = RED)
        reps = 0
    elif reps % 2 == 0 :
        countdown(short_break_sec)
        label.config(text = "BREAK", fg = PINK)
    else:
        countdown(work_sec)
        label.config(text = "WORK", fg = GREEN)

def reset_timer():
    # canvas.itemconfig(timer_text, text = "00:00")
    # window.after(1000, countdown, 0)
    pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    seconds = count % 60
    minutes = count // 60
    if seconds < 10:
        seconds = f'0{seconds}'
        
    if minutes == 0 and seconds == 0:
        reps += 1
    
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0 :
       window.after(2, countdown, count - 1)
    else:
        start_timer()

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