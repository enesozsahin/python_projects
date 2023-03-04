from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

current_card={}
should_learn={}

try:
    data=pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    main_data=pd.read_csv("spanish_words.csv")
    should_learn=main_data.to_dict(orient="records")
else:
    should_learn= data.to_dict(orient="records")

# ----------------functions-----------------------
def generate_word():
    global current_card,timer
    window.after_cancel(timer)
    current_card= random.choice(should_learn)
    canvas.itemconfig(title_text, text="Spanish",fill="black")
    canvas.itemconfig(word_text,text=current_card["Spanish"],fill="black")
    canvas.itemconfig(background,image=card_front_image)
    timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(background, image=card_back_image)

def is_known():
    should_learn.remove(current_card)
    print(len(should_learn))
    data2=pd.DataFrame(should_learn)
    data2.to_csv("words_to_learn.csv",index=False)
    generate_word()



window=Tk()
window.title("FlashCardSpanish")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# this variable and its path !!! important
timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800, height=526)
card_front_image= PhotoImage(file= "card_front.png")

card_back_image = PhotoImage(file="card_back.png")

background =canvas.create_image(400,263,image=card_front_image)
title_text=canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross= PhotoImage(file="wrong.png")
wrong_button = Button(image=cross,highlightthickness=0,command=generate_word)
wrong_button.grid(row=1,column=0)
wrong_button.config(bg=BACKGROUND_COLOR)

check= PhotoImage(file="right.png")
right_button= Button(image=check,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)


generate_word()


window.mainloop()


# another way to convert the data to a list of dicts
# data = pd.read_csv('spanish_words.csv')
# dict={rows.Spanish:rows.English for index,rows in data.iterrows()}
# word_list=[]
#
# for sp,en in dict.items():
#     words={sp:en}
#     word_list.append(words)