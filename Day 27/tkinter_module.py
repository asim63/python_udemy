import tkinter


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 400)


my_label = tkinter.Label(text = "I am Asim", font = ("Arial", 24, "bold"))
my_label.pack(side = 'left')


window.mainloop()
    