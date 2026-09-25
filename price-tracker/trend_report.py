import pandas as pd
from datetime import date, timedelta

print("=== MOSH APP - PRICE TREND REPORT ===\n")

data = []
with open("prices.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        # If old data has 3 parts, add today's date
        if len(parts) == 3:
            item, price, location = parts
            date_val = date.today().strftime("%Y-%m-%d") 
        else:
            item, price, location, date_val = parts
        data.append([item.title(), int(price), location.title(), date_val])

df = pd.DataFrame(data, columns=["Item", "Price", "Market", "Date"])

# Get this week vs last week
today = date.today()
last_week = today - timedelta(days=7)

this_week_avg = df[df["Date"] >= last_week.strftime("%Y-%m-%d")].groupby("Item")["Price"].mean()
last_week_avg = df[df["Date"] < last_week.strftime("%Y-%m-%d")].groupby("Item")["Price"].mean()

if len(this_week_avg) == 0 or len(last_week_avg) == 0:
    print("Not enough data yet. Add prices for 2 different weeks to see trends.")
else:
    for item in this_week_avg.index:
        if item in last_week_avg.index:
            change = ((this_week_avg[item] - last_week_avg[item]) / last_week_avg[item]) * 100
            arrow = "📈" if change > 0 else "📉"
            print(f"{arrow} {item}: {change:+.1f}%")
            print(f" Last Week: ₦{last_week_avg[item]:,.0f} | This Week: ₦{this_week_avg[item]:,.0f}\n")

print("=== END TREND REPORT ===")