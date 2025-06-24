#if-else statements

entry_price = 1000
exit_price = 1500

if entry_price < exit_price:
    print("Profit")
else:
    print("Loss")

    
entry_price2 = int(input("Enter the entry price of the stock: "))
exit_price2 = int(input("Enter the exit price of the stock: "))

if entry_price2 < exit_price2:
    print("Profit")
else:
    print("Loss")



    # if-elsif-else statements

    
stop_loss = int(input("Enter the stop loss price of the stock: "))

if entry_price2 < exit_price2:
    print("Profit")
elif exit_price2 > stop_loss:
    print("Stop Loss Triggered")
else:
    print("No Profit No Loss")



    
