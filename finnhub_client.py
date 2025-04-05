import finnhub
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")
client = finnhub.Client(api_key=api_key)
