from nse_data import get_index_price, atm_strike

INDEX = "SENSEX"      # change to BANKNIFTY later if needed
STRIKE_STEP = 100     # SENSEX step

print("🛕 Barsana started")

price = get_index_price(INDEX)

if price is None:
    print("❌ NSE live data not available. Stop.")
    exit()

strike = atm_strike(price, STRIKE_STEP)

print(f"{INDEX} Live Price:", price)
print("Suggested Option:", f"{INDEX} {strike} CE")
print("Bias: BUY CALL")
print("Risk: 20%")
print("Target: 30%")
print("⚠️ Manual trade only")
import time

print("Barsana worker started...")

while True:
    time.sleep(30)
