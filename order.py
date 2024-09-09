
from customer import Customer
from coffee import Coffee

class Order:
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
                raise ValueError("price must be between 1.0 and 10.0.")
        except ValueError:
            raise ValueError("Price must be a valid float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)

  # retrieve the customer who placed the order.
    @property
    def customer(self):
        return self._customer
  # Getting the type of coffee in the order.
    @property
    def coffee(self):
        return self._coffee
 # Getting the price of the order returnig the float: Price of the order
    @property
    def price(self):
        return self._price