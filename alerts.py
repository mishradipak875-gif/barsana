import requests

BOT_TOKEN = "8475545907:AAFpcVMaXwkWhavOzGW_QuQJqhCOII_gKJY"
CHAT_ID = "1288789590"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    r = requests.post(url, data=payload)
    print("Telegram response:", r.text)
