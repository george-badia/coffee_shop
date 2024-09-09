import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation():
    # Test case to create an Order instance and validate its details.
    customer = Customer("Lavenda")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_invalid_price():
    # Test case to ensure ValueError is raised for an invalid order price.
    customer = Customer("Lavenda")
    coffee = Coffee("Macchiato")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)