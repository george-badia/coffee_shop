class Coffee:
    def __init__(self, name):

        # validate and raise valueError: If the coffee name is empty
        if not name:
            raise ValueError("Coffee name cannot be empty")
        self.name = name
        self.orders = []  

# retrieves the number of orders for this coffee.
    def num_orders(self):
         
        
        return len(self.orders)

  # Calculate the average price of orders for this coffee.
    def average_price(self):
        
        # this will return average price, or 0 if there are no orders
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders) if self.orders else 0

    # Get a list of customers who ordered this coffee.
    def customers(self):
       
        # it will return a List of Customer objects
        return [order.customer for order in self.orders]


    # Add an order to this coffee's list of orders. and has a Parameters Order object to add to the list of orders
    def add_order(self, order):
        
        self.orders.append(order)  