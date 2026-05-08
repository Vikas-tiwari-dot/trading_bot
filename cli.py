import argparse

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def print_summary(args):
    print("\n========== ORDER SUMMARY ==========")
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Order Type  : {args.order_type}")
    print(f"Quantity    : {args.quantity}")

    if args.order_type.upper() == "LIMIT":
        print(f"Price       : {args.price}")

    print("===================================\n")


parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading pair e.g. BTCUSDT"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--order_type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Price for LIMIT orders"
)

# IMPORTANT
args = parser.parse_args()

try:
    validate_symbol(args.symbol)
    validate_side(args.side)
    validate_order_type(args.order_type)
    validate_quantity(args.quantity)
    validate_price(args.price, args.order_type)

    print_summary(args)

    client = BinanceFuturesClient().get_client()

    order_manager = OrderManager(client)

    if args.order_type.upper() == "MARKET":
        response = order_manager.place_market_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            quantity=args.quantity
        )

    else:
        response = order_manager.place_limit_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            quantity=args.quantity,
            price=args.price
        )

    print("ORDER PLACED SUCCESSFULLY\n")

    print("=========== RESPONSE ===========")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice')}")
    print("================================")

except Exception as e:
    print(f"ERROR: {e}")