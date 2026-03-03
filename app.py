import requests
import time

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

def check_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

while True:
    print("---- Tarama Başladı ----")
    for symbol in SYMBOLS:
        price = check_price(symbol)
        print(f"{symbol} fiyat: {price}")
    print("------------------------")
    time.sleep(60)
