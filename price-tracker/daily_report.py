import pandas as pd
from datetime import date

print("=== GENERATING WHATSAPP REPORT ===\n")

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

# Get today's prices
today_str = date.today().strftime("%Y-%m-%d")
today_df = df[df["Date"] == today_str]

# Build WhatsApp message
report = f"""*📊 MOSH MARKET DATA - MARKET REPORT - {today_str}*
*Your #1 Source for Food Prices in Lagos*

"""

for index, row in today_df.iterrows():
    report += f"*{row['Item']}*: ₦{row['Price']:,} - {row['Market']}\n"

report += f"""
*🚨 DEALS FOUND:*
Run price_alert.py to see where to buy cheap!

To subscribe weekly: DM ₦500 
Powered by MOSH MARKET DATA
"""

# Save to file
with open("whatsapp_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("REPORT READY!")
print("Open 'whatsapp_report.txt' and copy everything to WhatsApp")
print("\n" + "="*40)
print(report)