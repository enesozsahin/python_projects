import tkinter as tk
from tkinter import *
from budget_functions import *
import pandas as pd
import matplotlib.pyplot as plt

createdatabase()
name = ""
lastname= ""
def addoperation():
    global name
    global lastname
    name = ent3.get()

    lastname = ent4.get()
    income = ent5.get()
    expense_amount = ent2.get()
    budget_goal = ent6.get()


    if (name == "Enter your name"):
        print("Please write a name")
        open_error_win()
    elif (lastname == "Enter your lastname"):
        print("Please write a lastname")
        open_error_win()
    elif (income == "Enter your income"):
        print("Please write a income")
        open_error_win()
    elif (expense_amount == "Enter expense amount"):
        print("Please write a expense amount")
        open_error_win()
    elif (budget_goal == "Set a budget goal"):
        print("Please write a budget goal")
        open_error_win()
    else:
        insert(name, lastname, income, clicked.get(), expense_amount, budget_goal)
        print("Operation is successfully added")
        data = getdata(name, lastname)
        df = pd.DataFrame(data, columns=['Expense_For', 'Expense'])
        grouped_df = df.groupby('Expense_For').sum()
        grouped_df.plot.pie(y='Expense', autopct='%1.1f%%')
        plt.show()
        print(grouped_df)
        print(data)
    return True






win = Tk()
frm1 = Frame(win)
frm1.pack(side=tk.LEFT, padx=20)

var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

ent2 = Entry(frm1, textvariable=var2)
var2.set("Enter expense amount")
ent2.grid(row=8, column=1)

ent3 = Entry(frm1, textvariable=var3)
var3.set("Enter your name")
ent3.grid(row=2, column=1)

ent4 = Entry(frm1, textvariable=var4)
var4.set("Enter your lastname")
ent4.grid(row=4, column=1)

ent5 = Entry(frm1, textvariable=var5)
var5.set("Enter your income")
ent5.grid(row=6, column=1)

ent6 = Entry(frm1, textvariable=var6)
var6.set("Set a budget goal")
ent6.grid(row=10, column=1)


def show():
    label8.config(text=clicked.get())

# Dropdown menu options
options = [
    "Food & Drink",
    "House Expenses",
    "Travel Expenses",
    "Market",
    "Taxes & Legal Expenses",
    "Health & PersonalCare"]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Select Category")

# Create Dropdown menu
drop = OptionMenu(win, clicked, *options)
drop.place(x=260, y=135)

# Create button, it will change label text
button = Button(win, text="click Me", command=show)
button.place(x=290, y=170)

# Create Label
label8 = Label(win, text=" ")
label8.place(x=275, y=200)


def open_sec_win():
    # declare the window
    window = Tk()
    # set window title
    window.title("User Info")
    # set window width and height
    window.configure(width=500, height=300)
    # set window background color
    window.configure(bg='lightgray')

    frm2 = Frame(window)
    frm2.pack()

    # Retrieve data from the database
    data = getdata(name, lastname)

    # Create labels for the table headers
    header1 = tk.Label(frm2, text="Expense For")
    header1.grid(row=0, column=0)
    header2 = tk.Label(frm2, text="Expense Amount")
    header2.grid(row=0, column=1)

    # Iterate through the data and create a new row for each item
    for i, row in enumerate(data):
        expense_for = tk.Label(frm2, text=row[0])
        expense_for.grid(row=i+1, column=0)
        expense_amount = tk.Label(frm2, text=row[1])
        expense_amount.grid(row=i+1, column=1)



btn = Button(frm1, text="Add Operation", command=addoperation)
btn.grid(row=14, column=1)

btn2 = Button(frm1, text= "User Info", command= open_sec_win)
btn2.grid(row=25, column=15 )


win.title("PersonalBudgetApp")
win.geometry("500x400")
win.resizable(False, False)
win.mainloop()



