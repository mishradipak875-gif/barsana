import os
import requests

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

BASE_URL = "https://api.dhan.co/v2"

HEADERS = {
    "access-token":eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzcwNjE4Mzk2LCJpYXQiOjE3NzA1MzE5OTYsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTEwMzI4NjM5In0.XbJGRGVMkWqDg1BET9ovOxd0Qo9mtnJn_P5ncjSiUbkYIcNSH_EG4hIwyx42MpAbPqge9u2hIUyHgJh9M_k9BA ,
    "client-id": 1110328639,
    "Content-Type": "application/json"
}

def get_index_price(symbol):
    url = f"{BASE_URL}/market/ltp"

    payload = {
        "securities": {
            "BSE": [symbol]
        }
    }

    r = requests.post(url, json=payload, headers=HEADERS, timeout=10)
    r.raise_for_status()
    data = r.json()

    return data["data"]["BSE"][symbol]["last_price"]


def atm_strike(price, step):
    return round(price / step) * step
