import schedule
import time
from update_nifty50_list import update_nifty_list
from save_nifty50_ohlcv import fetch_and_save_all_ohlcv

# # 🗓 Weekly NIFTY 50 update every Sunday at 09:00 AM
# schedule.every().sunday.at("09:00").do(update_nifty_list)

# 📊 OHLCV fetch job every 1.5 minutes
schedule.every(0.5).minutes.do(fetch_and_save_all_ohlcv)

print("✅ Scheduler started. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)