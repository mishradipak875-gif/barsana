def pick_option(index, option_type):
    index_price = {
        "NIFTY": 22550,
        "BANKNIFTY": 48200,
        "SENSEX": 74200,
        "BANKEX": 52500
    }

    lot_size = {
        "NIFTY": 50,
        "BANKNIFTY": 15,
        "SENSEX": 10,
        "BANKEX": 15
    }

    price = index_price[index]
    strike = round(price / 100) * 100

    if option_type == "BUY CALL":
        option_name = f"{index} {strike} CE"
    elif option_type == "BUY PUT":
        option_name = f"{index} {strike} PE"
    else:
        return None, None

    option_price = round(price * 0.005, 2)  # simulated premium

    return option_name, option_price
