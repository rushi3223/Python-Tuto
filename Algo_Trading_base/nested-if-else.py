# nested if-else statements

entry_price = int(input("Enter the entry price of the stock: "))
exit_price = int(input("Enter the exit price of the stock: "))
stop_loss = int(input("Enter the stop loss price of the stock: "))

if entry_price < exit_price:
    print("Profit")
elif exit_price > stop_loss:
    print("Stop Loss Triggered")
else:
    print("No Profit No Loss")
    if exit_price - entry_price > 100:
        print("High Profit")
    elif exit_price - entry_price < 50:
        print("Low Profit")
    else:
        print("Moderate Profit")


#while statements

current_price = 150 
target_price  = 155

while current_price < target_price:
    print("Price is still below the target price")


    current_price += 1

# After the loop ends, we can assume the price is now above the target price
    print("Now the Price is above the target price and you can sell the stock")


   