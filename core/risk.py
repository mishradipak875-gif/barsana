def risk_check(option):
    if option == "WAIT":
        print("No trade allowed ❌")
        return

    entry = 120
    stop_loss = entry * 0.8
    target = entry * 1.3

    print("Entry:", entry)
    print("Stop Loss:", stop_loss)
    print("Target:", target)
    print("Trade Allowed ✅")
