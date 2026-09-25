import pandas as pd
from datetime import date
import sys

print("=== MOSH MARKET DATA - LOGIN REQUIRED ===")
users = {
    "mosh_ceo": "1234",
    "trader_ade": "5678",
    "trader_bola": "9999",
    "yunus": "7777"
}
username = input("Enter username: ")
password = input("Enter password: ")

if username not in users or users[username]!= password:
    print("\n❌ Access Denied. Subscribe: DM ₦500 to 080-XXX-XXXX")
    sys.exit() # Kick them out

print(f"\n✅ Welcome {username}! Generating report...\n")