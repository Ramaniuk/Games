import tkinter
from tkinter import constants
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {
        website_data: {
            "email": user_data,
            "password": password_data,
        }
    }

    if website_data == "" or user_data == "" or password_data == "":
        messagebox.showinfo(title="Error", message="Please don't leave empty field(s)")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, constants.END)
            password_entry.delete(0, constants.END)


# ---------------------------FIND PASSWORD------------------------------------
def search_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            key = website_entry.get()
            value_password = data[key]["password"]
            value_email = data[key]["email"]
    except KeyError:
        messagebox.showinfo(title="Error", message="There is no such data")
    else:
        messagebox.showinfo(title="Password",message=f"The data for {key} is\n"
                                                     f"password: {value_password}\n"
                                                     f"email: {value_email}")


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

website_entry = tkinter.Entry(width=21)
website_entry.focus() #cursor in the entry field
website_entry.grid(row=1, column=1)

search_button = tkinter.Button(text="Search",width=13, command=search_password)
search_button.grid(row=1, column=2)

user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = tkinter.Entry(width=35)
user_entry.insert(0, "Olga@gmail.com") # constants.END - last index, after text
user_entry.grid(row=2, column=1, columnspan=2)

password = tkinter.Label(text="Password:")
password.grid(row=3,column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3,column=1)

password_button = tkinter.Button(text="Generate Password",command=password_generator)
password_button.grid(row=3,column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()