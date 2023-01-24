import datetime as dt
import sqlite3 as sql
from tkinter import *
import tkinter.messagebox as messagebox

def insert(name,lastname,ıncome,expense_for,expense,budget_goal):
    conn = sql.connect("PersonalBudgetingApp.db")
    cursor = conn.cursor()
    current_time = dt.datetime.now().time().strftime("%H:%M:%S")
    add_comment = """INSERT INTO PERSONAL VALUES {}"""
    data = (name,lastname,ıncome,expense_for,expense,budget_goal,current_time)
    print("New data saved successfully")
    cursor.execute(add_comment.format(data))
    conn.commit()
    conn.close()


def getdata(name,lastname):
    conn = sql.connect("PersonalBudgetingApp.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Expense_For, Expense FROM PERSONAL WHERE Name = ? AND Lastname = ?", (name, lastname))
    data = cursor.fetchall()
    return data
    conn.close()

def createdatabase():
    conn = sql.connect("PersonalBudgetingApp.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS PERSONAL(
        Name text,
        Lastname text,
        Income float,
        Expense_For text,
        Expense float,
        Budget_Goal integer,
        Time text)
    """)

    conn.commit()
    conn.close()


def open_error_win():
    messagebox.showerror("Error", "Please enter a valid value")




