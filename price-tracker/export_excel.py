import pandas as pd

print("Loading MOSH APP data...")

data = []
with open("prices.txt", "r") as file:
    for line in file:
        item, price, location, date = line.strip().split(",")
        data.append([item.title(), int(price), location.title()])

df = pd.DataFrame(data, columns=["Item", "Price", "Market", "Date"])

# Make it look pretty
df = df.sort_values("Price")

df.to_excel("MOSH_Report.xlsx", index=False)

print("Report exported! File: MOSH_Report.xlsx")
print(df)