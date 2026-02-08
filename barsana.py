import time
from dhan_client import get_index_price
from alerts import send_telegram

INDEX_MAP = {
    "NIFTY": "NIFTY 50",
    "BANKNIFTY": "NIFTY BANK",
    "SENSEX": "SENSEX",
    "BANKEX": "BANKEX"
}

print("✅ BARSANA STARTED")

last_signal = {}

while True:
    try:
        for name, symbol in INDEX_MAP.items():
            price = get_index_price(symbol)

            trend = "BULLISH" if price % 2 == 0 else "BEARISH"
            signal = "BUY CALL" if trend == "BULLISH" else "BUY PUT"

            if last_signal.get(name) != signal:
                msg = f"""🛕 Barsana LIVE Alert
Index: {name}
Price: {price}
Signal: {signal}
"""
                send_telegram(msg)
                last_signal[name] = signal

        time.sleep(60)  # check every 1 minute

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
