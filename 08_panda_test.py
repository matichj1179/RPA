import pandas


ingredient = ["heavy whipping cream", "mascarpone", "granulated sugar", "vanilla extract", "cold espresso", "coffee flavored liqueur", "cocoa powder", "lady fingers"]
amount_needed = [357, 226.8, 66.67, 4, 354.88, 45, 10, 200]
amount_used =[500, 500, 1000, 50, 500, 700, 375, 200]
price = [8.89, 8.89, 2.70, 4.79, 4.00, 36.99, 6.49, 5.50]

RPA_dict = {
    "Ingredients": ingredient,
    "Amount_needed": amount_used,
    "Amount_used": amount_used,
    "Price": price
}

RPA_frame = pandas.DataFrame(RPA_dict)

print(RPA_frame)
