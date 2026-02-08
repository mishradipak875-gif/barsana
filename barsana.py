import time

print("✅ BARSANA STARTED")

while True:
    try:
        print("⏳ alive")

        # ---- YOUR MAIN LOGIC CALL ----
        # Example:
        # run_strategies()
        # fetch_nse_data()
        # process_signals()

    except KeyError as e:
        print(f"❌ KeyError missing key: {e}")
        time.sleep(15)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        time.sleep(15)

    time.sleep(10)
