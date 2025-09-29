# Hint: Market conditions are unpredictable - you monitor until something happens
stock_symbol = input("Enter stock symbol: ")
current_price = float(input("Enter starting price: "))
target_price = float(input("Enter target price: "))
stop_loss = float(input("Enter stop-loss price: "))

price_updates = 0
alert_triggered = False
# Think: What approach handles unpredictable market timing?
# Your monitoring logic here

while not alert_triggered:
    new_price = float(input("Enter new price: "))
    price_updates += 1
    current_price = new_price
#if the current price is greater tha the target then the target has been reached
    if current_price >= target_price:
        print("Target reached")
        alert_triggered = True
        #if current price is is less than stop loss then the stop loss is triggered
    elif current_price <= stop_loss:
        print("Stop-loss triggered")
        alert_triggered = True
    else:
        #otherwise print update count and price
        print(f"Price update {price_updates}: {current_price} ")




      