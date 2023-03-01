from tkinter import *
from tkinter import messagebox
import random
# copies to the clipboard automatically
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    [password_list.append(random.choice(letters)) for b in range(random.randint(8, 10))]

    [password_list.append(random.choice(symbols)) for b in range(random.randint(2, 4))]

    [password_list.append(random.choice(numbers)) for b in range(random.randint(2, 4))]

    random.shuffle(password_list)

    # Instead of a list, it gathers all the characters into a string just by adding nothing between them.
    password= "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    w=website_entry.get()
    e=email_username_entry.get()
    p=password_entry.get()

    iscont=messagebox.askokcancel(title=w , message=f"Are you sure you want to continue with the info entered ?"
                                             f" \nEmail:{e} \nPassword:{p}" )

    if len(w)==0 or len(e)==0 or len(p)==0:
        messagebox.showerror(title="Error!", message="Please make sure you fill all the fields.")

    elif iscont:

        with open("data.txt","a") as data:
            data.write(w+" | "+e+" | "+p+"\n")
        website_entry.delete(0,END)
        email_username_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("PassHawk Password Manager")
window.config(padx=50,pady=50)

canvas =Canvas(width=200,height=200)
# logo1=PhotoImage(file="PASS HAWK without hawk.png")
logo=PhotoImage(file="PassHawkLogo.png")
canvas.create_image(70,100,image=logo)
canvas.grid(row=0, column=1)

website_label= Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label= Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label= Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry= Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

email_username_entry= Entry(width=35)
email_username_entry.grid(row=2,column=1, columnspan=2)

website_entry= Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

generate_password_button= Button(text="Generate Password",width=14,command=generate_password)
generate_password_button.grid(row=4,column=2)


add_button= Button(text="Add Password",width=30,command=save)
add_button.grid(row=5,column=1,columnspan=2)

window.mainloop()