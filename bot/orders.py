from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(
                f"Placing MARKET order | Symbol={symbol} | Side={side} | Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Market Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
            raise