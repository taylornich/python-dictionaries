# question 1 task 1

restaurant_menu = {
    "Starters": {"Soup":5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#adding a category
restaurant_menu["Beverages"] = {"Juice": 1.99, "Fountain Drink": 2.99}

#updating
menu_change = {"Steak": 17.99}
restaurant_menu["Main Course"].update(menu_change)

#removing
removed_item = restaurant_menu["Starters"].pop("Bruschetta")


print(restaurant_menu)

