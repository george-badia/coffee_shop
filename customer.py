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

# Find the customer who spent the most on a specific coffee.
    @staticmethod
    def most_aficionado(coffee):
       
        # while passing Parameters as :
        # - coffee: which is an object to find the aficionado for the customer who spent the most on the specified coffee ,keeping in mind max value which is an initial comparison point to find the maximum price among orders for a specific coffee by customers
        max_price = float('-inf')
        aficionado = None
        for customer in Customer.customers:
            for order in customer.order_list:
                if order.coffee == coffee and order.price > max_price:
                    max_price = order.price
                    aficionado = customer
        return aficionado

# Initialize an Order instance with a customer, coffee, and price.while passin customers who placed their orders ,coffee types being offered and price in float (objects)as parameters
class Order:
    def __init__(self, customer, coffee, price):
        
        self.customer = customer
        self.coffee = coffee
        self.price = price 