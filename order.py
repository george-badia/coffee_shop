from customer import Customer
from coffee import Coffee

class Order:
    #  to a list store all Order instances
    all_orders = []

#Initializing an Order instance with a customer, coffee, and price.the price here should be in float or convertible to float representing the price of the order (between 1.0 and 10.0)
    def __init__(self, customer, coffee, price):
       

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)
