import pandas


# Functions go here

# Checks user answer yes / no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response in ["yes", "y"]:
            return "show instructions"

        elif response in ["no", "n"]:
            return ""

        else:
            print("please answer yes / no")


# Checks user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
            print()
        else:
            return response


# Checks that user enters a valid number
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


# Main routine goes here
show_instructions = yes_no("Do you want to see the instructions? ")

if show_instructions == "show instructions":
    print("Instructions go here")
print()

recipe_name = not_blank("Please enter recipe name: ")
print()

servings = num_check("How many servings? ", "Please enter a number more than 0", int)
print()

ingredient_list = []
amount_bought_list = []
amount_used_list = []
price_list = []
cost_to_make_list = []

# Loop to use ingredients
while True:
    name = not_blank("Please enter ingredient name or 'xxx' to quit: ")
    print()
    if name == 'xxx':
        print("We are done")
        break

    units = not_blank("What units is it in? (ml, g, kg, l): ")
    print()

    amount = num_check(f"How many {units}'s did you buy? ", "Please enter a valid amount", float)
    print()

    amount_used = num_check(f"How many {units}'s did you use? ", "Please enter a valid amount", float)
    print()

    cost = num_check("How much?: $", "Please enter a valid amount", float)
    print()

    if units == "kg":
        amount = amount * 1000
    elif units == "l":
        amount = amount * 1000

    if units == "kg":
        amount_used = amount_used * 1000
    elif units == "l":
        amount_used = amount_used * 1000

    # Calculate cost to make for this ingredient
    cost_to_make = (cost / amount) * amount_used

    # Append data to lists
    ingredient_list.append(name)
    amount_bought_list.append(amount)
    amount_used_list.append(amount_used)
    price_list.append(cost)
    cost_to_make_list.append(cost_to_make)

# Create DataFrame after the loop
RPA_dict = {
    "Ingredients": ingredient_list,
    "Amount_bought": amount_bought_list,
    "Amount_used": amount_used_list,
    "Price": price_list,
    "Cost_to_make": cost_to_make_list
}

RPA_frame = pandas.DataFrame(RPA_dict)

# Calculate total cost
total = RPA_frame['Cost_to_make'].sum()

# Calculate per serving
per_serve = total / servings

# Printing area
print(recipe_name)
print(f"Servings: {servings}")
print(RPA_frame)
print(f"Total cost: ${total:.2f}")
print(f"Per Serve: ${per_serve:.2f}")
