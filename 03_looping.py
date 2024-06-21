# main routine starts here

# set max amount of ingredients here
MAX_INGREDIENTS = 3

# loop to use ingredients
ingredients_used = 0
while ingredients_used < MAX_INGREDIENTS:
    name = input("Please enter ingredient name or 'xxx' to quit ")

    if name == 'xxx':
        break

    ingredients_used += 1

# output number of ingredients sold
if ingredients_used == MAX_INGREDIENTS:
    print("Congratulations you have used all your ingredients")
else:
    print(f"You have used {ingredients_used} ingredient/s. There is {MAX_INGREDIENTS - ingredients_used} ingredient/s remaining")
