# Phase-3-wk2-Code-Challenge


# Restaurants

Welcome to the "Restaurants" project! This project is a simulation of a Yelp-style domain involving three main entities: `Customer`, `Restaurant`, and `Review`. The goal of this simulation is to demonstrate the relationships between customers, restaurants, and reviews, and to showcase various functionalities related to these entities.

## Table of Contents

- [Introduction](#introduction)
- [Classes](#classes)
- [Methods](#methods)
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this simulation, we have three main classes:

1. `Customer`: Represents a customer who can write reviews for restaurants.
2. `Restaurant`: Represents a restaurant that can be reviewed.
3. `Review`: Represents a review written by a customer for a restaurant.

These classes are interconnected through various relationships, and the simulation demonstrates how they interact with each other.

## Classes

### Customer

The `Customer` class represents an individual who can write reviews. It has the following attributes and methods:

- Attributes:
  - `given_name`: Given name of the customer.
  - `family_name`: Family name of the customer.
  - `reviews`: List of reviews written by the customer.
  - `all_customers`: Keeps track of all created customer instances.

- Methods:
  - `given_name()`, `family_name()`, and `full_name()`: Accessors for the customer's names.
  - `add_review(restaurant, rating)`: Creates a new review associated with the customer and a restaurant.
  - `restaurants()`: Returns a list of restaurants reviewed by the customer.
  - `num_reviews()`: Returns the total number of reviews written by the customer.
  - `find_by_name(name)`: Class method to find a customer by their full name.
  - `find_all_by_given_name(given_name)`: Class method to find all customers with a given given name.

### Restaurant

The `Restaurant` class represents a restaurant that can be reviewed. It has the following attributes and methods:

- Attributes:
  - `name`: Name of the restaurant.
  - `all_restaurants`: Keeps track of all created restaurant instances.

- Methods:
  - `name()`: Accessor for the restaurant's name.
  - `reviews()`: Returns a list of reviews for the restaurant.
  - `customers()`: Returns a list of customers who reviewed the restaurant.
  - `average_star_rating()`: Calculates the average star rating for the restaurant.
  - `all()`: Class method to get a list of all restaurant instances.

### Review

The `Review` class represents a review written by a customer for a restaurant. It has the following attributes and methods:

- Attributes:
  - `_customer`: The customer who wrote the review.
  - `_restaurant`: The restaurant being reviewed.
  - `_rating`: The rating given by the customer.
  - `all_reviews`: Keeps track of all created review instances.

- Methods:
  - `rating()`: Accessor for the review's rating.
  - `get_all_reviews()`: Class method to get a list of all review instances.
  - `customer()`: Returns the customer associated with the review.
  - `restaurant()`: Returns the restaurant associated with the review.

## Usage

The simulation demonstrates the relationships between customers, restaurants, and reviews. It includes functionalities such as adding reviews, calculating average ratings, and finding customers and restaurants based on specific criteria.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the provided code in your preferred Python environment to explore the simulation.

## Contributing

Contributions to this project are welcome! Feel free to open issues or pull requests if you have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Author
It is written by Philip Ogaye.
