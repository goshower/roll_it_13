
def int_check():
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



#main routine stars here
game_goal = int_check()
print(game_goal)

