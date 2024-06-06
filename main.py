from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Reference from day 5 code
def generate_password():
    """Generates a random password and inserts it into the password entry box."""
    lowerletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Combine all character sets into a single list
    character_pool = lowerletters + upperletters + numbers + symbols

    # Select characters randomly and ensure at least one from each set
    password_length = 13
    password = []
    for char_set in [lowerletters, upperletters, numbers, symbols]:
        password.append(random.choice(char_set)) # Guarantee at least one from each set, only 4 char
    password += random.choices(character_pool, k=password_length - len(password))  # Fill remaining characters

    # Concatenates all the elements of a string array, using the specified separator between each element
    password = ''.join(password)

    # Insert the generated password into the password entry box
    password_entry.delete(0, END)  # Clear any existing content
    password_entry.insert(0, password)
    pyperclip.copy(password) # pyperclip automatically copy the pw and ready to paste

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = website_entry.get().lower()
    email_data = email_entry.get()
    password_data = password_entry.get()

    # Create the format for JSON, this is essentially a dictionary
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0 :
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            clear()

def find_password():
    try:
        website_data = website_entry.get().lower()

        # Retrieve JSON data from the file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        # Access and process the retrieve JSON data
        retrieved_email = data[website_data]["email"]
        retrieved_password = data[website_data]["password"]

        # pop up info
        messagebox.showinfo(title="Credential", message=f"Credential for '{website_data.capitalize()}'"
                                                        f"\nYour Email : {retrieved_email}\n Your Password: {retrieved_password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"No details for {website_data.capitalize()} exists.")


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passport Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label=Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label =Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus() # Greet the user with the cursor in this input dialog

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alvin@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan= 1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()