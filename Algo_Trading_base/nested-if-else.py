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
