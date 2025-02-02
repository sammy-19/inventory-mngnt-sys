from prettytable import PrettyTable

# For processing data entered by the user
class Stock:
    def __init__(self, products, headers):
        self.__products = products
        self.headers = headers
        self.__products

# Restocking product quantities
    def restocking(self, key, value):
        
        # Searches for a product in a dictionary of products
        if key in self.__products:
            print(self.__products[key])
            self.__products[key][0] += value
            self.__products[key][-1] += (value*self.__products[key][-2])
            return self.__products
        else:
            print("No such product")
            
# To display the data stored in products variable             
    def product_output(self):
        #self.headers.before("S/N", 0)
        table = PrettyTable()
        table.field_names = self.headers
        
        # Unpacking the products and quantities into separate lists for display in tabular form
        for key, value in self.__products.items():
            names, qtys =[], []
            names.append(key)
            qtys.append(value)
            
            # appends a product name into a temporary list created  in order to add a row in order to add the product and its particulars
            for p, q in zip(names, qtys):
                q.insert(0, p)
                table.add_row(q)
                q.pop(0)
        return table

# Removing a certain quantity of a product out of the system: Outstocking
    def out_stocking(self, prd, qty):
        
        # checking if a product is present then outstock
        if prd in self.__products.keys():
            self.__products[prd][0] -= qty
            #self.__products[prd][-1] -= (qty*+self.__products[prd][-2])
            print(f'{self.__products[prd][0]}  Remaining\n')
        else:
            print('No such product')
            pass
        return self.__products
        
if __name__ == "__main__":
    dict = {'a':[10, 11, 12], 'b':[1, 2, 3], 'c':[3, 4, 5]}
    h = [1, 2, 3, 4]
    stock = Stock(dict, h)
    #out_stk = stock.out_stocking('a', 5)
    print(stock.product_output())
    restock = stock.restocking('a', 6)
    print(stock.product_output())