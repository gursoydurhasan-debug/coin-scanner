import requests

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

def check_price(symbol: str) -> float:
    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": "linear", "symbol": symbol}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()

    if data.get("retCode") !=
