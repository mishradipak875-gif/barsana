def option_signal(signal):
    if signal == "BUY":
        decision = "BUY CALL"
    elif signal == "SELL":
        decision = "BUY PUT"
    else:
        decision = "WAIT"

    print("Option Decision:", decision)
    return decision
