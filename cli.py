from binance.client import Client
import argparse
import logging
from logging_config import setup_logging

setup_logging()

# API KEYS (use env variables ideally)
api_key = "enter api key "
api_secret = "enter api secreat"

client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# CLI setup
parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

# VALIDATION
if args.type == "LIMIT" and args.price is None:
    raise ValueError("Price required for LIMIT orders")

try:
    # MARKET ORDER
    if args.type == "MARKET":
        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type=args.type,
            quantity=args.quantity
        )

    # LIMIT ORDER
    else:
        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type=args.type,
            quantity=args.quantity,
            price=str(args.price),
            timeInForce="GTC"
        )

    # LOGGING (after order created)
    logging.info(f"Order request: {args}")
    logging.info(f"Order response: {order}")

    print("✅ Order placed!")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

except Exception as e:
    logging.error(f"Error: {e}")
    print("❌ Error:", e)