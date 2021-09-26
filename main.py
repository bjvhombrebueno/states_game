import pandas
import turtle
screen = turtle.Screen()
screen.screensize(1200,600)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_states=[]
missed_states =[]
score = 0
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the state",prompt="What's another state's name").title()
    print(answer_state)
    if answer_state =="Exit":
        break
    if answer_state in all_states:
        #write guess in map
        if answer_state.title() in correct_states:
            pass
        else:
            correct_states.append(answer_state)
            score += 1

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states_data[states_data.state == answer_state]
            x = int(state_data.x)
            y = int(state_data.y)
            t.goto(x=x,y=y)
            t.write(state_data.state.item())

missed_states = [my_state for my_state in all_states if my_state not in correct_states]
missed_states_file = pandas.DataFrame(missed_states)
missed_states_file.to_csv("missed_states.csv")



screen.exitonclick()
