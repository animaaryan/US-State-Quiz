import turtle

import pandas

# Print to the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle
writer = turtle.Turtle()
writer.color("red")
writer.hideturtle()
writer.penup()

# Create a score turtle
wrong_guess = turtle.Turtle()
wrong_guess.color("red")
wrong_guess.hideturtle()
wrong_guess.penup()

# Create a good turtle
right_guess = turtle.Turtle()
right_guess.color("green")
right_guess.hideturtle()
right_guess.penup()

# Add a user guess
user_guess = ""

# Pull the states from the csv
states = pandas.read_csv("50_states.csv")

# Store the states in a variable
all_states = states['state'].tolist()

# Store the user guesses into a list
correct_guesses = []

# Score tracking
score = 0

# Run a while loop
while score < 50:

    # Show a guess window on the screen
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?")

    # Clear existing
    wrong_guess.clear()
    right_guess.clear()

    # Convert to title case
    if not answer_state:

        # Loop through all the states to check which are missing
        missing_states = [state for state in all_states if states not in correct_guesses]

        # Create a new csv file to add the missing states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Convert to title case
    user_guess = answer_state.title()

    # Check if the user guess is correct and then add it to the list
    if user_guess in all_states:

        # Find the x and y coordinates of the maps using the loc and iloc functions
        x = states.loc[states["state"] == user_guess]["x"].iloc[0]
        y = states.loc[states["state"] == user_guess]["y"].iloc[0]

        # Store the correct guesses in a list
        if user_guess not in correct_guesses:
            correct_guesses += [user_guess]

            # Tell user they rock
            right_guess.goto(0, 250)
            right_guess.write("Good Guess!", align="center", font=("Georgia", 15, "bold"))

            # Write the correct guess onto the map
            writer.goto(x, y)
            writer.write(user_guess, align="center", font=("Georgia", 8, "bold"))

            # Increase the score value
            score += 1
    else:
        wrong_guess.goto(0, 250)
        wrong_guess.write("Incorrect Guess", align="center", font=("Georgia", 15, "bold"))

screen.exitonclick()
print(correct_guesses)
