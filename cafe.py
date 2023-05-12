# Task on Dictionaries and lists

print("Here is the total stock worth for your cafe.")

menu =["coffee", "cupcake", "Tea", "Americano", "Wallnut cake"]         # Create a list of items
price = {"coffee":1.50, "cupcake":2, "Tea":1.20,"Americano":1.60, "Wallnut cake": 3.20}  # create a dictionary of the items and their price, the items should match with each other to evoid error
stock = {"coffee":300, "cupcake":150, "Tea":200,"Americano":160, "Wallnut cake":120}        # create a dictionary of the items and their stock

item_value = 0      # Defining a variable that contain the total value of each items
total_budget = 0       # Defining a variable that will contain the total of all items together, this is not mendatory

# Itering trough the dictionaries using the keys from the list

for key in menu:        
    item_value = price[key]*stock[key]
    total_budget += item_value 
   
print(f"The total stock worth in the cafe is: {total_budget}")  # Finally print the final result

    



    
    