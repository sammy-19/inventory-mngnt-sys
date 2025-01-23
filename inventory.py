import sys
from stock import Stock
   
# A dictionary for storing and accessing the items
storage = {}
            
print("Welcome to Inventory Managment App\nWhat do you want to do? follow the prompt below\n")

# A loop that is running the entire program
# Gets the response from the user, compares it to the response for execution
while True:
    response = input("s to stock in products, r for restocking, o for outstocking, v for viewing the inventory or q to quit: ")
    
    # Stocking In new items
    if response == "s":
        
        # Number to determine the number of items a user is entering 
        num = int(input('\nEnter Number of the types of products to store: '))
        
        # Entering & Storing the items based on a number specified by user
        while num > 0:
            prd, qty = input("Product Name: ").strip(), int(input("Quantity: "))
            storage[prd] = qty
            num -= 1
        stock = Stock(storage)

# Restocking of items                        
    elif response == "r":
            print("\n\nRestocking...")
            prd, qty = input("Product Name: "), int(input("Quantity: "))
            stock.restocking(prd, qty)
            print("Success\n")
    
 # Outstocking/decreasing the quantity of items
    elif response == 'o':
        print('Outstocking...')
        prd, qty = input("Product Name: "), int(input("Quantity: "))
        stock.out_stocking(prd, qty)

# Displaying all the stored items together with their quantities                
    elif response == 'v':
            print(stock.product_output())

# Exiting the application                        
    elif response == 'q':
        print("Thank You For the operations")
        sys.exit()