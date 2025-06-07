# Step 2: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}
# Step 3: Get user input
portfolio = {}

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Step 4: Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock}: {quantity} shares × ₹{price} = ₹{value}")
    total_investment += value

print(f"\nTotal Investment: ₹{total_investment}")

