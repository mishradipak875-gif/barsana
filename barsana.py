import os
import time
import requests
from datetime import datetime

# =========================
# TELEGRAM FUNCTION
# =========================
def send_telegram(message: str):
    token = os.getenv("8475545907:AAG228X4fjTNPj2vlkhbifnP5K_lNnix-h4")
    chat_id = os.getenv("1288789590")

    if not token or not chat_id:
        print("❌ Telegram env vars missing")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            print("📨 Telegram message sent")
        else:
            print(f"❌ Telegram error: {r.text}")
    except Exception as e:
        print(f"❌ Telegram exception: {e}")


# =========================
# BARSANA START
# =========================
print("✅ BARSANA STARTED")
send_telegram("🚀 BARSANA LIVE ON RAILWAY")


# =========================
# MAIN LOOP (KEEP ALIVE)
# =========================
while True:
    try:
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"⏳ alive | {now}")

        # ----------------------------------
        # PLACE STRATEGY CODE HERE LATER
        # ----------------------------------
        # Example (future):
        # signal = check_market()
        # if signal:
        #     send_telegram(signal)

        time.sleep(60)  # VERY IMPORTANT (prevents Railway restart)

    except Exception as e:
        print(f"❌ Runtime error: {e}")
        send_telegram(f"❌ Barsana error: {e}")
        time.sleep(30)
