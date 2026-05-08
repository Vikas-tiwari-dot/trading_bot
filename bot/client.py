import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API credentials missing in .env file")

        self.client = Client(api_key, api_secret)

        # Binance Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client