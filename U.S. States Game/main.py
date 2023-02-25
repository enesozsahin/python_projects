import turtle
import pandas

screen= turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

list2=[]

data=pandas.read_csv("50_states.csv")
states=data["state"]

for a in states:
    list2.append(a)

list= sorted(list2)
print(list)


correct_guesses=0

iscont= True
while iscont:
    answer_state = screen.textinput(title=f"Guess the State {(correct_guesses)}/50 ", prompt="What's another state's name?")
    answer=answer_state.title()

    if answer=="Exit":
        missed_states=pandas.DataFrame(list)
        missed_states.to_csv("states_to_learn.csv")

        break


    if answer in list:

        correct_guesses +=1

        index_answer = int(list.index(answer))
        print(answer)

        answer_x=(data["x"][index_answer])
        answer_y = (data["y"][index_answer])

        answer2 = turtle.Turtle()
        answer2.penup()
        answer2.hideturtle()
        answer2.goto(answer_x,answer_y)
        answer2.write(answer)
        answer2.goto(0,0)
        list.remove(answer)

    if correct_guesses==50:
        turtle3=turtle.Turtle()
        turtle3.penup()
        turtle3.hideturtle()
        turtle3.goto(0,0)
        turtle3.write("CONGRATS! YOU HAVE CORRECTLY GUESSED ALL THE STATES CORRECTLY")




