from tkinter import *

def button_clicked():
    #you can change text like this as well
    my_label.config(text = input.get())
    
window = Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 400)

#label
my_label = Label(text = "i am a Label", font = ("Arial", 24, "bold"))
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)
#button
button = Button(text = "Click me", command = button_clicked) #tkinter.Button
button.grid(column = 1, row = 1 )

#entry
input = Entry(width = 20)
input.grid(column = 3, row = 2)

#new_button
new_button = Button(text="new button")
new_button.grid(column = 2, row = 0)
new_button.config( padx = 5, pady = 5)
window.mainloop()
    
