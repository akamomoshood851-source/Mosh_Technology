print("=== MOSH MARKET DATA - VIEW MARKET DATA ===\n")

file = open("prices.txt", "r")
lines = file.readlines()
file.close()

if len(lines) == 0:
    print("No data yet! Run price_tracker.py first")
else:
    all_items = []
    all_prices = []
    
    print("All Saved Prices:")
    print("--------------------")
    for line in lines:
        item, price, location, date = line.strip().split(",")
        price = int(price) # turn "35000" into 35000
        print(f"Item: {item} | Price: ₦{price} | Market: {location}")
        all_items.append(item)
        all_prices.append(price)
    
    print(f"\nTotal Records: {len(lines)}")
    print(f"Average Price of all items: ₦{sum(all_prices) // len(all_prices)}")
    
    print("\n" + "="*30)
while True:
    search = input("Search for item (or type 'quit' to exit): ").title()
    
    if search == "Quit":
        print("Thanks for using MOSH APP!")
        break

    found = False
    for line in lines:
        item, price, location, date = line.strip().split(",")
        if item == search:
            print(f"Found: {item} is ₦{price} at {location}")
            found = True
    
    if found == False:
        print(f"No data for {search} yet")
        
        print("\n" + "="*30)
    item_check = input("Find cheapest market for: ").title()
    
    cheapest_price = 99999
    cheapest_location = ""
    
    for line in lines:
        item, price, location, date = line.strip().split(",")
        price = int(price)
        if item == item_check:
            if price < cheapest_price:
                cheapest_price = price
                cheapest_location = location
    
    if cheapest_location != "":
        print(f"Cheapest {item_check}: ₦{cheapest_price} at {cheapest_location}")
    else:
        print(f"No data for {item_check}")