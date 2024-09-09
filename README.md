# Coffee Shop Domain Modeling

Welcome to the Coffee Shop Domain Modeling project! This Python project uses Object-Oriented Programming (OOP) principles to simulate the operations of a coffee shop, focusing on the relationships between customers, coffee, and orders.

#### By **George Badia**

This project was created and is the sole property of George Badia.

## Project Overview

The Coffee Shop Domain Modeling project models a basic domain for a coffee shop, with three primary classes:

- **Customer**: Represents a customer who can place orders.
- **Coffee**: Represents different types of coffee available at the shop.
- **Order**: Represents an order made by a customer for a particular coffee.

### This project also simulates the relationships between these entities:

- A customer can place multiple orders.
- A coffee can have many orders.
- Each order belongs to one customer and one coffee.

## Features

**Customer Management**: Create customers with names that are validated for length.
**Coffee Management**: Define various coffee types with proper validation.
**Order System**: Customers can place multiple orders for different coffees, each with a specific price.
**Data Aggregation**: Calculate the number of orders for each coffee and find the customer who has spent the most on a specific coffee.
**Test Coverage**: All methods and classes are tested using pytest.

## Setup/Installation Requirements

- Linux or WSL for Windows users
- Visual Studio Code installed
- GitHub account
- Python 3.x

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/george-badia/coffee_shop
   ```
2. Navigate to the repository directory:
   ```bash
   cd <repository_name>
   ```
3. Open in Vs code or your desired IDE:
   ```bash
   $ code .
   ```

## Running the Application

1. Ensure Python 3.x is installed on your machine.

2. Set Up the Virtual Environment: This project uses `pipenv` for managing dependencies:

   ```bash
   $ pipenv install
   $ pipenv shell
   ```

3. Run the test cases for validation:
   ```bash
   $ pytest
   ```
4. Run the script :If you're using Python 3 and the default python command refers to Python 2, you may need to use:
   ```bash
   $ python3 debug.py
   ```

## Technologies Used

This program is built with:

- python3
- Visual Studio Code environment

## Support and Contact Details

For any issues, please email me at george.otieno1@student.moringaschool.com

## License

This project is licensed under the MIT License.
