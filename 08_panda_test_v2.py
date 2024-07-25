import pandas


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

recipe_name = not_blank("Please enter recipe name: ")
print()

Servings = num_check("how many servings? ", "please enter a number more than 0", int)
print()

ingredient_list = []
amount_bought_list = []
amount_used_list = []
price_list = []

# loop to use ingredients
while True:

    name = not_blank("Please enter ingredient name or 'xxx' to quit: ")
    print()
    if name == 'xxx':
        print("We are done")
        break
    units = not_blank("what units is it in? (ml, g, kg, l): ")
    print()
    if units == 'xxx':
        print("We are done")
        break
    amount = num_check(f"how many {units}'s did you buy ", "please enter a valid amount", float)
    print()
    if amount == 'xxx':
        print("We are done")
        break
    amount_used = num_check(f"how many {units}'s did you use ", "please enter a valid amount", float)
    print()
    if amount == 'xxx':
        print("We are done")
        break
    cost = num_check("how much?: ", "please enter a valid amount", float)
    print()
    if cost == 'xxx':
        print("We are done")
        break

    if units == "kg":
        converted_grams = units * 1000

    if units == "l":
        converted_millilitres = units * 1000

        # Append data to lists
    ingredient_list.append(name)
    amount_bought_list.append(amount)
    amount_used_list.append(amount_used)
    price_list.append(cost)

# Create DataFrame after the loop
RPA_dict = {
    "Ingredients": ingredient_list,
    "Amount_bought": amount_bought_list,
    "Amount_used": amount_used_list,
    "Price": price_list
}

RPA_frame = pandas.DataFrame(RPA_dict)

# convert units ie: Kg to g and L to ml


# calculate the cost of each ingredient
cost_to_make = RPA_frame['Price'] / RPA_frame['Amount_bought'] * RPA_frame['Amount_used']

# calculate total cost
total = cost_to_make.sum()

# printing area
print(recipe_name)
print(f"Servings:{Servings}")
print(RPA_frame)
print(f"{cost_to_make:.2f}")
print(f"Total cost:${total:.2f}")
