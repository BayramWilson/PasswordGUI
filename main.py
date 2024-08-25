from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
LABEL_FONT = ("Courier", 14, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """It picks up 8-9 letters 2-3 symbols and numbers, puts them to a list shuffle the list and copies it to the
    entry and your keyboard"""
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# IF ADD BTN USED
def save():
    """takes the inputs from entries, write them to the data.txt file, clears the entries"""
    data = open("data.txt", "a")
    # get value from entry points
    website = entry_website.get()
    name = entry_name.get()
    password = entry_password.get()
    if website == "" or password == "":
        messagebox.showerror(title="Oops", message="You forgot some information")
    elif messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {name} "
                                                       f"\nPassword: {password} \n Is it ok to save?"):
        data.write(f"{website} | {name} | {password} \n")
        data.close()
        entry_website.delete(0, END)
        entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# create canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# create Label(Website / Email/Username / Password)

website_label = Label(text="Website:", font=LABEL_FONT)
website_label.grid(column=0, row=1)

name_label = Label(text="Email/Username:", font=LABEL_FONT)
name_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=LABEL_FONT)
password_label.grid(column=0, row=3)

# create an Entry Object
entry_website = Entry(width=35)
entry_name = Entry(width=35)
entry_password = Entry(width=21)
# create inputs
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_name.grid(column=1, row=2, columnspan=2)
entry_name.insert(0, "bayram.wilson04@gmail.com")
entry_password.grid(column=1, row=3)


# create buttons passwordgen & Add
button_passwordgen = Button(text="Generate Password", command=generate_password)
button_passwordgen.grid(column=2, row=3)

button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2)
button_add.config(width=36)

window.mainloop()
