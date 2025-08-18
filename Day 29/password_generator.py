from tkinter import *
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = input1.get()
    email_name = input2.get()
    password = input3.get()
    
    with open("Day 29/ data.txt", mode = 'a') as file:
        file.write(f"{website_name} | {email_name} | {password}\n")
        input1.delete(0,END)
        input3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = YELLOW)


canvas = Canvas(width = 200, height = 200, highlightthickness = 0, bg = YELLOW)
logo_image = PhotoImage(file = r"Day 29\logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row = 0, column = 1)
#label-website
website = Label(text= "Website:", bg = YELLOW)
website.grid(row = 1, column = 0)

#label-email
email = Label(text = "Email/Username:",bg = YELLOW)
email.grid(row = 2, column = 0)

#label-password
pw = Label(text = "Password:", bg = YELLOW)
pw.grid(row = 3, column = 0)

#entry-1
input1 = Entry(width = 52)
input1.grid(row = 1, column = 1, columnspan = 2)
input1.focus()

#entry-2
input2 = Entry(width = 52)
input2.insert(END, "asim@gmail.com")
input2.grid(row = 2, column = 1, columnspan = 2)

#entry-3 
input3 = Entry(width = 33)
input3.grid(row = 3, column = 1)

#button-1 
genpw = Button(text = "Generate Password ", command = generate_pw)
genpw.grid(row = 3, column = 2)

#button-2
add = Button(text = "Add", width = 44, command = save)
add.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()