
#mainly 2 loops in python
# for loop and while loop

# for loop
# for loop iterates over a sequence (like a list, tuple, or string) or other iterable objects
# and executes a block of code for each item in the sequence.

 # While Else with Example

price = [120,112,114,111,112]
thresold_price = 115
index = 0 

while index < len(price):
    if price[index] > thresold_price:
        print(f"The price  {price[index]} breaches the thresold price {thresold_price} at {index}  ")
        break
    index += 1
else:
    print("There is no price breach")

print("Search is completed")
