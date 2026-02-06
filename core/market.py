def market_trend(index_name):
    prices = {
        "NIFTY": (22540, 22510),
        "BANKNIFTY": (48200, 48050),
        "SENSEX": (74200, 74120),
        "BANKEX": (52500, 52380)
    }

    price_now, price_before = prices[index_name]

    if price_now > price_before:
        trend = "BULLISH"
    elif price_now < price_before:
        trend = "BEARISH"
    else:
        trend = "SIDEWAYS"

    print(f"{index_name} Trend:", trend)
    return trend
