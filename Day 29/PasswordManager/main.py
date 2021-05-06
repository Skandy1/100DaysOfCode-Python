from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os

GREEN = "#0fd93b"
BLUE = "#718beb"
CYAN = "#48e8cd"


# ---------------------------- OPEN FILE ------------------------------- #
def openfil():
    os.system("notepad data.txt")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = entry_website.get()
    user_email = entry_email.get()
    user_password = entry_password.get()
    if len(user_password) == 0 or len(user_website) == 0 or len(user_email) == 0:
        messagebox.showerror(title="Error", message="All fields are mandatory!!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm",
                                       message=f" Website:{user_website}\n Email: {user_email}\n "
                                               f"Password:{user_password}")
        if is_ok:
            data_file = open("data.txt", "a")
            data_file.write(user_website + " --- " + user_email + " --- " + user_password + "\n")
            data_file.close()
            entry_password.delete(0, END)
            entry_website.delete(0, END)
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(bg="white")
window.config(padx=50, pady=50)

# canvas with image
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# label website
label_website = Label(text="Website")
label_website.grid(row=1, column=0)

# label email
label_email = Label(text="Email/Username")
label_email.grid(row=2, column=0)

# label password
label_password = Label(text="Password")
label_password.grid(row=3, column=0)

# Entry website
entry_website = Entry(width=40)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

# Entry email
entry_email = Entry(width=40)
entry_email.insert(END, "skanda@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)

# Entry password
entry_password = Entry(width=22)
entry_password.grid(row=3, column=1, columnspan=1)

# button generate
button_generate = Button(text="Generate Password", command=generate_password, bg=BLUE)
button_generate.grid(row=3, column=2)

# button add
button_add = Button(text="ADD", width=36, command=save, bg=GREEN)
button_add.grid(row=4, column=1, columnspan=2)

# button my passwords
button_mypass = Button(text="My Saved Password", command=openfil, bg=CYAN, width=36)
button_mypass.grid(row=5, column=1, columnspan=2)

window.mainloop()
