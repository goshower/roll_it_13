
error = "Please enter an interger more than / equal to 13."

while True:
    try:
        game_goal = int(input("What is the game goal"))
        print(f"Game goal: {game_goal}")
        if game_goal < 13:
            print(error)
        else:
            print(f"Game goal:{game_goal}")
            break

    except ValueError:
        print(error)

