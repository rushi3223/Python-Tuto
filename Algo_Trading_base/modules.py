import math

math.floor(11.5)
math.ceil(11.5)

print(math.floor(11.5))   # Rounds down to the nearest integer
print(math.ceil(11.5))    # Rounds up to the nearest integer

math.sqrt(16)  # Returns the square root of 16

math.pow(2, 3)  # Returns 2 raised to the power of 3
math.pow(10, 3)  # Returns 10 raised to the power of 3
print(math.sqrt(16))  # Outputs: 4.0
print(math.pow(10, 3))  # Outputs: 1000.0  
print(math.pow(2, 3))  # Outputs: 8.0

import keyword

# List of Python keywords

print(keyword.kwlist)  # Outputs the list of Python keywords
# Example of using a keyword
if True:
    print("This is a valid use of the 'if' keyword.")

    import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)  # Outputs a random integer between 1 and 10
# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)  # Outputs a random float between 0 and 1   


# Generate a random choice from a list
choices = ['apple', "banana", 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
random_choice = random.choice(choices)
print(random_choice)  # Outputs a random choice from the list

import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)  # Outputs the current date and time 


# Stock Price Simulation Example
import random
import datetime

#initial stock pricer and volatility
initial_price = 100.0
volatility = 0.02  # 2% daily volatility

volatility_change = random.choice([-volatility, volatility])  # Random change in price

daily_price_change = initial_price + (initial_price * volatility_change)

today = datetime.datetime.now()
print("Todays date and time:", today)
print("Initial stock price:", initial_price)
print("Daily price change:", daily_price_change)


help ("modules") # Displays help information about modules