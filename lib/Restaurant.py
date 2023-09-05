class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

    def restaurants(self):
        return [review.restaurant() for review in Review.get_all_reviews() if review.customer() == self]

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name() == given_name]


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name

    def reviews(self):
        return [review for review in Review.get_all_reviews() if review.restaurant() == self]

    def customers(self):
        return list(set([review.customer() for review in self.reviews()]))

    def average_star_rating(self):
        restaurant_reviews = [review.rating() for review in self.reviews()]
        if restaurant_reviews:
            return sum(restaurant_reviews) / len(restaurant_reviews)
        return 0

    @classmethod
    def all(cls):
        return cls.all_restaurants


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant


# Create instances for the customers and the restaurants
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Tasty Eats")
restaurant2 = Restaurant("Cozy Corner")


# Add reviews using the add_review method
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer1.add_review(restaurant2, 3)


# Print the restaurants associated with each customer and their ratings
print(f"Restaurants reviewed by {customer1.full_name()}:")
for restaurant in customer1.restaurants():
    review = [review for review in Review.get_all_reviews() if review.customer() == customer1 and review.restaurant() == restaurant][0]
    print(f"- {restaurant.name()}: Rating {review.rating()}")

print(f"Restaurants reviewed by {customer2.full_name()}:")
for restaurant in customer2.restaurants():
    review = [review for review in Review.get_all_reviews() if review.customer() == customer2 and review.restaurant() == restaurant][0]
    print(f"- {restaurant.name()}: Rating {review.rating()}")

# Print the customers who reviewed each restaurant and their ratings
print(f"Customers who reviewed {restaurant1.name()}:")
for customer in restaurant1.customers():
    review = [review for review in Review.get_all_reviews() if review.customer() == customer and review.restaurant() == restaurant1][0]
    print(f"- {customer.full_name()}: Rating {review.rating()}")

print(f"Customers who reviewed {restaurant2.name()}:")
for customer in restaurant2.customers():
    review = [review for review in Review.get_all_reviews() if review.customer() == customer and review.restaurant() == restaurant2][0]
    print(f"- {customer.full_name()}: Rating {review.rating()}")
