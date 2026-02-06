import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(HEADERS)

def init_nse():
    try:
        session.get("https://www.nseindia.com", timeout=5)
        time.sleep(1)
    except:
        pass

def get_index_price(symbol, retries=3):
    for attempt in range(1, retries + 1):
        try:
            init_nse()
            url = "https://www.nseindia.com/api/allIndices"
            r = session.get(url, timeout=5)

            if r.status_code != 200:
                raise Exception("Bad status")

            data = r.json()["data"]
            for item in data:
                if symbol.upper() in item["index"]:
                    return float(item["last"])

        except Exception as e:
            print(f"⚠️ NSE attempt {attempt} failed, retrying...")
            time.sleep(2 * attempt)

    return None

def atm_strike(price, step):
    return round(price / step) * step
