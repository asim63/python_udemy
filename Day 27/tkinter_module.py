from tkinter import *


window = Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 400)


my_label = Label(text = "I am Asim", font = ("Arial", 24, "bold"))
my_label.pack()


#button
def button_clicked():
    #you can change text like this as well
    my_label['text'] = input.get()
    my_label.pack()

button = Button(text = "Click me", command = button_clicked) #tkinter.Button
button.pack()


#entry

input = Entry(width = 20)
input.pack()


window.mainloop()
    
