import pandas as pd
from datetime import date

print("=== MOSH MARKET DATA - PRICE ALERT SYSTEM ===\n")
print("Checking for good deals...\n")

# Load data
data = []
with open("prices.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            item, price, location = parts
            date_val = date.today().strftime("%Y-%m-%d")
        else:
            item, price, location, date_val = parts
        data.append([item.title(), int(price), location.title(), date_val])

df = pd.DataFrame(data, columns=["Item", "Price", "Market", "Date"])

# Get only today's prices
today = date.today().strftime("%Y-%m-%d")
today_data = df[df['Date'] == today]

deals_found = False

# Find cheapest for each item today
for item in today_data['Item'].unique():
    item_prices = today_data[today_data['Item'] == item]
    if len(item_prices) > 1:  # Only if 2+ markets have it today
        cheapest = item_prices.loc[item_prices['Price'].idxmin()]
        expensive = item_prices['Price'].max()
        savings = expensive - cheapest['Price']
        if savings > 0:
            deals_found = True
            print(f"BEST DEALS TODAY:")
            print(f"{item}: ₦{cheapest['Price']:,} at {cheapest['Market']} [Cheapest - Save ₦{savings:,}]")

if not deals_found:
    print("No deals right now. Prices are normal.")

print("\n=== END REPORT ===")