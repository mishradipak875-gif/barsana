sent = False

while True:
    try:
        if not sent:
            send_telegram("🚀 Barsana running on Railway")
            sent = True

        print("⏳ alive")

    except Exception as e:
        print(e)

    time.sleep(10)
