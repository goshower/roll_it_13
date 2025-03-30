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


#Main routine

#testing loop
while True:
   want_instructions = yes_no("Do you want to see the instructions?")
   print(f"you chose {want_instructions}")

print("we done")



