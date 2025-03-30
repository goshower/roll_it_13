#functions go here

def yes_no(question):
    while True:

        """ Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            print("you said no")
            return "no"
        else:
            print("please enter yes/no")

def instructions():...


def int_check():...
    """Checks users enter on eteger more than / equal to 13"""

    error = "Please enter an interger more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal"))
            print(f"Game goal: {response}")
            if response < 13:
                print(error)
            else:
              return response

        except ValueError:
            print(error)


#Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions?")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)






