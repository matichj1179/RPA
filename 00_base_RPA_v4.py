# functions go here

# Checks user answer yes / no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "show instructions"

        elif response == "no" or response == "n":
            return ""

        else:
            print("please answer yes / no")


# checks user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine goes here
show_instructions = yes_no("Do you want to see the instructions? ")

print(show_instructions)

# ask for the name of the recipe
recipe_name = not_blank("Please enter recipe name: ")

# loop to use ingredients
while True:
    name = not_blank("Please enter ingredient name or 'xxx' to quit ")

    if name == 'xxx':
        print("We are done")
        break
