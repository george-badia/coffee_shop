class Customer:
    # List to store all Customer instances
    customers = [] 

 # Initialize a Customer instance with a name, parameters that is a  string representing the name of the customer (1 to 15 characters)
    def __init__(self, name):
       
        # Raises ValueError if name is empty, not a string, or length is not between 1 and 15 characters
        if not name or not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters")
        self.name = name
        # this will to store customer's orders and add the customer to the list of all customers
        self.order_list = []  
        Customer.customers.append(self) 

 # Create an order for the customer with the given coffee and price.
    def create_order(self, coffee, price):
       
        # Parameters:
        # - coffee: Coffee object is representing the type of coffee in the order
        # - price: which has to be float representing the price of the order
       
       #The created order which is retuned back
        order = Order(self, coffee, price)
        # Add the order to the coffee's list of orders
        coffee.add_order(order)  
        self.order_list.append(order)
        return order
# getting a list of orders placed by the customer,and returning a list of Order objects
    def orders(self):
        return self.order_list

# getting a list of coffee types ordered by the customer and also return a list of Coffee 
    def coffees(self):
         
        return [order.coffee for order in self.order_list]

 