import pytest
from coffee import Coffee
from customer import Customer
from order import Order

  # Test case to verify the creation of a Coffee instance.
def test_coffee_creation():
  
    coffee = Coffee("Macchiato")
    assert coffee.name == "Macchiato"

# Test case to ensure ValueError is raised for an invalid empty coffee name.
def test_invalid_coffee_name():

    with pytest.raises(ValueError):
        Coffee("")

 # Test case to check the number of orders for a specific coffee.
def test_num_orders():
   
    coffee = Coffee("Espresso")
    customer1 = Customer("obi")
    customer1.create_order(coffee, 5.0)
    assert coffee.num_orders() == 1

# Test case to calculate the average price of orders for a specific coffee.
def test_average_price():
    
    coffee = Coffee("Macchiato")
    customer1 = Customer("obi")
    customer1.create_order(coffee, 5.0)
    customer2 = Customer("Rubi")
    customer2.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.5


   # Test case to verify the list of customers who ordered a specific coffee.
def test_coffee_customers():
 
    coffee = Coffee("Macchiato")
    customer1 = Customer("obi")
    customer2 = Customer("Rubi")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    assert set(coffee.customers()) == {customer1, customer2}