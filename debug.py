
from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("=== Interactive Debugging Script for Customer, Coffee, and Order ===\n")

    # Create customers
    print("Creating customers...")
    Rubi = Customer("Rubi")
    obi = Customer("obi")
    print(f"Created customers: {Rubi.name}, {obi.name}\n")

    # Create coffee types
    print("Creating coffee types...")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    print(f"Created coffees: {espresso.name}, {latte.name}\n")

    # Customers placing orders
    print("Placing orders...")
    order1 = Rubi.create_order(espresso, 5.00)
    order2 = Rubi.create_order(latte, 4.50)
    order3 = obi.create_order(espresso, 6.00)
    print(f"Rubi placed an order for {order1.coffee.name} at ${order1.price}")
    print(f"Rubi placed an order for {order2.coffee.name} at ${order2.price}")
    print(f"obi placed an order for {order3.coffee.name} at ${order3.price}\n")

    # Check number of orders for each coffee
    print(f"Number of orders for Espresso: {espresso.num_orders()}")
    print(f"Number of orders for Latte: {latte.num_orders()}\n")

    # Check the average price for each coffee
    print(f"Average price for Espresso: ${espresso.average_price():.2f}")
    print(f"Average price for Latte: ${latte.average_price():.2f}\n")

    # List customers who ordered each coffee
    espresso_customers = espresso.customers()
    latte_customers = latte.customers()
    print(f"Customers who ordered Espresso: {[customer.name for customer in espresso_customers]}")
    print(f"Customers who ordered Latte: {[customer.name for customer in latte_customers]}\n")

    # Find most aficionado customer for Espresso
    most_espresso_aficionado = Customer.most_aficionado(espresso)
    print(f"Customer who paid the highest price for Espresso: {most_espresso_aficionado.name} at ${order3.price}\n")

    # List all orders for Rubi and obi
    print(f"Rubi's orders: {[order.coffee.name for order in Rubi.orders()]}")
    print(f"obi's orders: {[order.coffee.name for order in obi.orders()]}\n")

    # List all coffees ordered by Rubi and obi
    print(f"Rubi's coffees: {[coffee.name for coffee in Rubi.coffees()]}")
    print(f"obi's coffees: {[coffee.name for coffee in obi.coffees()]}\n")

if __name__ == "__main__":
    main()
