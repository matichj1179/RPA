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
            print()
        else:
            return response


# checks that user enters a valid number
def num_check(question, error, num_type):
    while True:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
show_instructions = yes_no("Do you want to see the instructions? ")

print(show_instructions)
print()

# ask for the name of the recipe
recipe_name = not_blank("Please enter recipe name: ")
print()

Servings = num_check("how many servings? ", "please enter a number more than 0", int)
print()

# loop to use ingredients
while True:

    name = not_blank("Please enter ingredient name or 'xxx' to quit: ")
    print()
    if name == 'xxx':
        print("We are done")
        break
    units = not_blank("what units is it in? (ml, g, kg, L): ")
    print()
    if units == 'xxx':
        print("We are done")
        break
    amount = num_check(f"how many {units}'s? ", "please enter a valid amount", float)
    print()
    if amount == 'xxx':
        print("We are done")
        break
    cost = num_check("how much?: ", "please enter a valid amount", float)
    print()
    if cost == 'xxx':
        print("We are done")
        break
