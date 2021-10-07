import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. guess game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()
right_answer = 0
guessed_states = []
while right_answer < 50:
    answer = screen.textinput(title=f"Guess the state? {right_answer}/50", prompt="What is the next US state? Type Exit to finish the game").lower().capitalize()
    if answer == "Exit":
        not_guessed_states = []
        for state in all_states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        new_data = pandas.DataFrame(not_guessed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        right_answer += 1
        index = all_states.index(answer)

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(x[index], y[index])
        state.write(f'{answer}', font=('Arial', 12, 'italic'), align='center')
        guessed_states.append(answer)



screen.exitonclick()
