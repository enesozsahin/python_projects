from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer1=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer1)
    label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
    canvas.itemconfig(timer,text="00:00")
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        countdown(long_break_secs)
        label.config(text="Break", bg=YELLOW, fg=PINK)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        label.config(text="Break", bg=YELLOW, fg=PINK)

    else:
        countdown(work_secs)
        label.config(text="Work", bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec =f"0{count_sec}"


    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1=window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("PomodoroApp")
window.config(padx=100, pady=50, bg=YELLOW)



canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
timer = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=1)



label= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
label.grid(row=0, column=1)



tick_label=Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14))
tick_label.grid(row=4, column=1)


reset_button= Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row=3, column=2)

start_button=Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3,column=0)



window.mainloop()