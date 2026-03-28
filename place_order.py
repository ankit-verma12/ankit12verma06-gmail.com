from binance.client import Client

api_key = "enter api key "
api_secret = "enter api secreat"

client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    order = client.futures_create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="LIMIT",
    quantity=0.005,
    price="30000",
    timeInForce="GTC"
)

    print("✅ MARKET Order placed!")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

except Exception as e:
    print("❌ Error:", e)