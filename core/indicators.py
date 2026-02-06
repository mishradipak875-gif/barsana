def indicator_signal(trend):
    if trend == "BULLISH":
        signal = "BUY"
    elif trend == "BEARISH":
        signal = "SELL"
    else:
        signal = "NO TRADE"

    print("Indicator Signal:", signal)
    return signal
