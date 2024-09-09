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
