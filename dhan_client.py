import requests
import os

DHAN_TOKEN = os.getenv("DHAN_TOKEN")  # set in Railway later
BASE_URL = "https://api.dhan.co/v2"
HEADERS = {
    "access-token": DHAN_TOKEN,
    "Content-Type": "application/json"
}

def test_connection():
    url = f"{BASE_URL}/funds"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return "✅ Dhan token is VALID & connected"
    return f"❌ Failed: {r.status_code} | {r.text}"

def get_index_price(symbol):
    url = f"{BASE_URL}/market-quote/ltp"
    payload = {
        "securities": {
            "IDX": [symbol]
        }
    }
    r = requests.post(url, json=payload, headers=HEADERS)
    data = r.json()
    return float(data["data"]["IDX"][symbol]["last_price"])
