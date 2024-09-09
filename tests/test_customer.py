import pytest
from customer import Customer
from coffee import Coffee
from order import Order

 # Test case to verify the creation of a Customer instance.
def test_customer_creation():
   
    customer = Customer("obi")
    assert customer.name == "obi"

# Test case to ensure ValueError is raised for an invalid empty customer name.
def test_customer_invalid_name():
    
    with pytest.raises(ValueError):
        Customer("")

# Test case to create an order for a customer and validate order details.
def test_create_order():
    
    customer = Customer("obi")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

# Test case to check the list of orders for a customer.
def test_customer_orders():
  
    customer = Customer("obi")
    coffee = Coffee("Macchiato")
    order = customer.create_order(coffee, 4.5)
    assert customer.orders() == [order]


# Test case to verify the set of coffees ordered by a customer.
def test_customer_coffees():
    
    customer = Customer("obi")
    coffee1 = Coffee("Macchiato")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 4.5)
    customer.create_order(coffee2, 5.0)
    assert set(customer.coffees()) == {coffee1, coffee2}

# Test case to find the customer with the most orders for a specific coffee.
def test_most_aficionado():
    
    customer1 = Customer("obi")
    customer2 = Customer("Rubi")
    coffee = Coffee("Macchiato")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    assert Customer.most_aficionado(coffee) == customer2