VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are allowed.")


def validate_side(side: str):
    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type: str):
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")