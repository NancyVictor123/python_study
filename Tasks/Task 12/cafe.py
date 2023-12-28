# Create a list called menu and update the list with cafe items
# Create two dictionaries called Stock and price to update the 
# corresponding values of available stock and respective price
# Enter into a for loop and loop through items in menu list
# Use the item in list as key and calculate respective item value
#by multiplying stock and price
# Add the item value of each item to calculate total stock value
# Print the total stock value

menu = ['Cappucino', 'Latte', 'Espresso', 'Croissant']
stock = {"Cappucino" : 10,
         "Latte" : 12,
         "Espresso" : 17,
         "Croissant" : 25
        }
price = {"Cappucino" : 3.99,
         "Latte" : 3.99,
         "Espresso" : 2.99,
         "Croissant" : 1.99
       }
total_stock = 0
item_value = 0
for item in menu:
    item_value = stock[item] * price[item]
    #print(f"The item value for {item} is {item_value:.2f}")
    total_stock += item_value
print(f"The total stock worth in cafe = £{total_stock:.2f}")
