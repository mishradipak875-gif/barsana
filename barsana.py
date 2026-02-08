import os
import time
import requests

print("✅ BARSANA STARTED")

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Telegram env vars missing")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            print("📨 Telegram message sent")
        else:
            print("❌ Telegram error:", r.text)
    except Exception as e:
        print("❌ Telegram exception:", e)

# =========================
# TEST TELEGRAM ON START
# =========================
send_telegram("🚀 Barsana is LIVE and Telegram is working!")

# =========================
# KEEP ALIVE LOOP
# =========================
while True:
    print("⏳ alive")
    time.sleep(10)
