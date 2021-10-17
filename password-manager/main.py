import tkinter
from tkinter import constants
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password) #copy password in buffer

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    user_data = user_entry.get()
    password_data = password_entry.get()

    if website_data == "" or user_data == "" or password_data == "":
        messagebox.showinfo(title="Error",message="Please don't leave empty field(s)")
    else:
        is_ok = messagebox.askokcancel(title=website_data,message=f"Login: {user_data}\n Password: {password_data}\n Is it OK to save?") #true or false
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_data} | {user_data} | {password_data}\n")
                website_entry.delete(0, constants.END)
                user_entry.delete(0, constants.END)
                password_entry.delete(0, constants.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200) #widget
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = tkinter.Entry(width=35)
website_entry.focus() #cursor in the entry field
website_entry.grid(row=1,column=1,columnspan=2)

user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2,column=0)

user_entry = tkinter.Entry(width=35)
user_entry.insert(0, "Olga@gmail.com") # constants.END - last index, after text
user_entry.grid(row=2,column=1,columnspan=2)

password = tkinter.Label(text="Password:")
password.grid(row=3,column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3,column=1)

password_button = tkinter.Button(text="Generate Password",command=password_generator)
password_button.grid(row=3,column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()