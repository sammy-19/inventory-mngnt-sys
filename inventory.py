import sys
import datetime
from stock import Stock

# Stocking in of products into the system
def stocking(s, headings):
        
        # creating a temporal list for values of key(product) in a dictionary
        list = []  
        prd = input("Product Name: ").strip()
        qty = int(input("Quantity: "))
        date = str(datetime.date.today())
        unit_price = int(input("Unit Price: "))
        amount = qty*unit_price
        list += qty, date, unit_price, amount
        
        # storing a list as a value of a key (prd) into a dictionary
        s[prd.capitalize()] = list
         
# A dictionary for storing and accessing the items
products = {}

#Table headers for distinguishing the columns and proper display of products using PrettyTables
t_headers = ["Name", "Quantity", "Date Entered", "Unit Price", "Total"]
error_msg = 2"\nError:Invalid Input! Please Enter appropriate Values\n"
stock = Stock(products, t_headers) 
           
print("Welcome to Inventory Managment App\nWhat do you want to do? follow the prompt below\n")

# A loop that is running the entire program
# Gets the response from the user, compares it to the response for execution
while True:
    response = input("s to stock in products, r for restocking, o for outstocking, v for viewing the inventory or q to quit: ")
    
    # Stocking In new items
    if response == "s":
        
        # Number to determine the number of items a user is entering
        try:
            num = int(input('\nEnter Number of the types of products to store: '))
        
        # Entering & Storing the items based on a number specified by user
            while num > 0:
                stocking(products, t_headers)            
                num -= 1
        except ValueError:
            print(error_msg)
 
# Restocking of items                        
    elif response == "r":
            print("\nRestocking...")
            try:
                prd, qty= input("Product Name: ").capitalize().strip(), int(input("Quantity: "))            
            except ValueError:
                print(error_msg)
            else:
                stock.restocking(prd, qty)
                print("Success\n")
    
 # Outstocking/decreasing the quantity of items
    elif response == 'o':
        print('Outstocking...')
        try:
            prd, qty = input("Product Name: "), int(input("Quantity: "))
        except ValueError:
            print(error_msg)
            stock.out_stocking(prd, qty)

# Displaying all the stored items together with their quantities                
    elif response == 'v':
            print(stock.product_output())

# Exiting the application                        
    elif response == 'q':
        print("Thank You For the operations")
        sys.exit()