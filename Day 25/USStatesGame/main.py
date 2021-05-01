import turtle, pandas
from turtle import Turtle, Screen
screen=Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
csv_file=pandas.read_csv("50_states.csv")
state_list=csv_file.state.to_list()
guessed_list=[]
total=50
guessed=0
is_on=True
while is_on:
    screen.update()
    answer=screen.textinput(title=f"{guessed}/{total}",prompt="State Name:").title()
    if answer=="Exit":
        missing_states=[]
        for states in state_list:
            if states not in guessed_list:
                missing_states.append(states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_States.csv")
        is_on=False
        break
    if answer in state_list:
        guessed+=1
        guessed_list.append(answer)
        new_turtle=Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        row=csv_file[csv_file.state==answer]
        new_turtle.goto(int(row.x),int(row.y))
        new_turtle.write(answer,align="center",font=("Arial",7,"normal"))
    if guessed==total:
        is_on=False
