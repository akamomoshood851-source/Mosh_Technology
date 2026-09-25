from datetime import date

today = date.today().strftime("%Y-%m-%d")

print("=== MOSH MARKET DATA - Price Tracker v2 ===")
item = input("Enter food item: ")
price = input("Enter price in Naira: ")
location = input("Enter market location: ")

# Now we save with DATE
with open("prices.txt", "a") as file:
    file.write(f"{item},{price},{location},{today}\n")

print(f"Price saved for {today}!")