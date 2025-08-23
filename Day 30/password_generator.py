from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
        #Password Generator Project
    import random
    input3.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    
    password_letters = [random.choice(letters) for i in range(nr_letters)]
    
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
       
    password_list = password_letters + password_symbols + password_numbers
    
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    input3.insert(0, string = password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = input1.get()
    email_name = input2.get()
    password_name = input3.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name,
        }
    }
    if website_name == "" or email_name == "" or password_name == "":
        messagebox.showerror(title = "Error 404", message = "Please dont leave any fields empty")
    
    else:
        with open("Day 30/ data.json", mode = 'r') as file:
            data = json.load(file)
            data.update(new_data)
            
        with open("Day 30/ data.json",mode = 'w') as file:
            json.dump(data, file, indent = 4)
        input1.delete(0,END)
        input3.delete(0,END)

def search():
    with open("Day 30/ data.json", mode = 'r') as file:
        website_name = input1.get()
        for key in json.load(file):
            if website_name == key:
                messagebox.Message(f"email : {key['email']}\npassword : {key['password']}")
        
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
input1 = Entry(width = 33)
input1.grid(row = 1, column = 1)
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

#button-3
search_web = Button(text = "Search",width = 15, command = search)
search_web.grid(row = 1, column = 2)


window.mainloop()