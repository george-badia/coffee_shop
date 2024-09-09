from customer import Customer
from coffee import Coffee

class Order:
    #  to a list store all Order instances
    all_orders = []

#Initializing an Order instance with a customer, coffee, and price.the price here should be in float or convertible to float representing the price of the order (between 1.0 and 10.0)
    def __init__(self, customer, coffee, price):
   # Validating and raising valueError: If customer is not an instance of Customer or coffee is not an instance of Coffee.     
 if not isinstance(customer, Customer):
            raise ValueError("Invalid customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee.")
        
        try:
         #validating if the price is not a valid float between 1.0 and 10.0,if not raise value error
            price = float(price)  
            if not (1.0 <= price <= 10.0):
                raise ValueError("Price must be between 1.0 and 10.0.")
        except ValueError:
            raise ValueError("Price must be a valid float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)
