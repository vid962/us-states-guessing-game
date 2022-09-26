import turtle
import pandas
import csv

score = 0
states_as_a_list = []
user_answer_history = []
not_guessed_states = []


game_is_ON = True
screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Games")
text = turtle.Turtle()

# my background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

while game_is_ON:

    states_as_a_list = list(data["state"])
    user_answer = (screen.textinput(title=f"Guess the state:  {score}/50",
                                    prompt="What's the another state's name?")).title()

    if score == len(states_as_a_list) or user_answer == "Exit":

        # states which user didn't guess
        not_guessed_states = [x for x in states_as_a_list if x not in user_answer_history]

        # exporting not guessed states
        with open('states_to_learn.csv', 'w', newline="") as myfile:
            wr = csv.writer(myfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            wr.writerows(not_guessed_states)

        game_is_ON = False


    if user_answer in states_as_a_list and user_answer not in user_answer_history:

        user_answer_history.append(user_answer)

        user_data = (data[data["state"] == user_answer])
        state_x_coordinates = int(user_data.x)
        state_y_coordinates = int(user_data.y)
        state_name = str(user_data.state)

        score += 1

        text.penup()
        text.hideturtle()
        text.goto(state_x_coordinates, state_y_coordinates)
        text.write(user_answer)


turtle.mainloop()

