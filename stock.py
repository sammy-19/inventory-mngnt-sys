from prettytable import PrettyTable

# For processing data entered by the user
class Stock:
    def __init__(self, products):
        self.__products = products

# Restocking product quantities
    def restocking(self, key, value):
        if key in self.__products:
            self.__products[key] += value
            return self.__products
            
# To display the data stored in products variable             
    def product_output(self):
        list = ["S/N", "Name", "Quantity"]
        table = PrettyTable()
        table.field_names = list
        p_names, p_qtys = [], []
        serial = 1
        
        # Unpacking the products and quantities into separate lists for display in tabular form
        for key, value in self.__products.items():
            p_names.append(key)
            p_qtys.append(value)   
        for p, q in zip(p_names, p_qtys):
            table.add_row([serial, p, q])
            serial += 1
        return table

# Removing a certain quantity of a product out of the system: Outstocking
    def out_stocking(self, prd, qty):
        
        # checking if a product is present then outstock
        if prd in self.__products.keys():
            self.__products[prd] -= qty
            print(f'{self.__products[prd]}  Remaining\n')
        else:
            print('No such product')
            pass
        return self.__products