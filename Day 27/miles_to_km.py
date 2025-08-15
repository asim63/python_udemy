from tkinter import *


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 350, height = 200)
window.config(padx = 30, pady = 30)
def get_result():
    my_label4.config(text = f"{round((int(input.get())*1.609),2)}")
    
#label (is equal to)
my_label1 = Label(text = "is equal to", font = ("Arial", 12))
my_label1.config(padx = 10, pady = 10)
my_label1.grid(column = 0, row =1)

#label (miles)
my_label2 = Label(text = "Miles", font = ("Arial", 12))
my_label2.grid(column = 2, row =0)
my_label2.config(padx = 5, pady = 5)

#label(Km)
my_label3 = Label(text = "Km", font = ("Arial", 12))
my_label3.grid(column = 2, row =1)
my_label3.config(padx = 5, pady = 5)
#label(result)
my_label4 = Label(text = '0', font = ("Arial", 12))
my_label4.grid(column = 1, row = 1)

#entry 
input = Entry(width = 15)
input.grid(column = 1, row = 0)

#button
button = Button(width = 10, text = "Calculate", font =("Arial", 12), command = get_result )
button.config(padx = 1, pady = 1)
button.grid(column = 1, row = 2)



window.mainloop()