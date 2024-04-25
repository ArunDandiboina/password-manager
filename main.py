import json
from tkinter import *
# import all classes and constants but not modules...
# so we import with name
from tkinter import messagebox
import random
import pyperclip

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- SEARCH ------------------------------- #
def search():
    web = entry1.get()
    if len(web) != 0:
        try:
            with open("data.json", 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            messagebox.showinfo(title="oops", message="There is no file! please save a entry first.")

        else:
            if web in data:
                email = data[web]['email']
                password = data[web]['password']
                pyperclip.copy(password)
                messagebox.showinfo(title="Application", message=f"Email : {email} \nPassword : {password}")
            else:
                messagebox.showinfo(title="oops", message=f"No details for {web} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    entry3.delete(0, END)
    hd = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    hd.extend(random.sample(letters, nr_letters))
    hd.extend(random.sample(symbols, nr_symbols))
    hd.extend(random.sample(numbers, nr_numbers))
    random.shuffle(hd)
    hez = ''.join(hd)
    entry3.insert(0, string=hez)
    pyperclip.copy(hez)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_det():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        # another messagebox for yes or no (you can implement it.)
        try:
            with open("data.json", 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)

    else:
        messagebox.showinfo(title="oops", message="please don't leave any fields empty.")


# ---------------------------- UI SETUP ------------------------------- #
# args and kwargs important.

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=30)

# canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

# Buttons
button = Button(text="Search", command=search, width=14)
button.grid(column=2, row=1, columnspan=1)

button1 = Button(text="Generate Password", command=generate)
button1.grid(column=2, row=3, columnspan=1)

button2 = Button(text="Add", width=41, command=save_det)
button2.grid(column=1, row=4, columnspan=2)

# Entries
entry1 = Entry(width=30)
entry1.grid(column=1, row=1)
entry1.focus()

entry2 = Entry(width=48)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(0, string="d.arun672002@gmail.com")

entry3 = Entry(width=30)
entry3.grid(column=1, row=3, columnspan=1)

window.mainloop()
