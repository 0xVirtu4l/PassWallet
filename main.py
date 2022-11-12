from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassowrd():
    copy_label = Label(text="Password Copied Successfully to Clipboard", fg="green", font="Helvetica20")
    copy_label.grid(row=5, column=1, columnspan=2, sticky="EW")
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range (random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range (random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range (random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
     # *****  Update V2 ****** #
    copy_label.after(2000,copy_label.destroy)
     # *****  Update V2 ****** #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={website:{"email":email,"password":password,}}
    if len(website) == 0 or len(email) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops there is an error",message="Erorr Code: PWER_001\n Please make sure you haven't left any fields empty.")
    else:
    # *****  Update V2 ****** #
        try:
          with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
         with open("data.json","w") as data_file:
             json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
             json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    # ***** Update V2 ****** #
# ---------------------------- FIND PASSWORD ------------------------------- #
# *****  Update V2 ****** #
def find_password():
    website = website_entry.get()
    try :
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops there is an error",message="Erorr Code: PWER_002\n No Data File FOUND !!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            email_entry.delete(0, END)
            email_entry.insert(0, email)
            password_entry.delete(0, END)
            password_entry.insert(0, password)
        if len(website) ==0:
            messagebox.showinfo(title="Oops there is an error",message="Erorr Code: PWER_001\n Please make sure you haven't left any fields empty.")
        elif website not in data:
            messagebox.showinfo(title="Oops there is an error", message="Erorr Code: PWER_003\n The Email and The Password Are Not In The Database!!")
# *****  Update V2 ****** #

# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("PassWallet")
window.config(pady=50,padx=50)
canvas = Canvas(height=200,width=200)
# Import Logo Image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)



#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,sticky="EW",pady=4)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2,sticky="EW",pady=4)
email_entry.insert(0, "example@mail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,sticky="EW",pady=4)

# Buttons
search_button = Button(text="Search",command=find_password)
search_button.grid(row=1, column=2,sticky="EW",pady=4,padx=4)
generate_password_button = Button(text="Generate Password",command=generatePassowrd)
generate_password_button.grid(row=3, column=2,sticky="EW",pady=4,padx=2)
add_button = Button(text="Add", width=36,command=savePassword)
add_button.grid(row=4, column=1, columnspan=2,sticky="EW")


window.mainloop()
