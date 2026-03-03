import requests

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

def check_price(symbol):
    url = "https://api.bybit.com/v5/market/tickers"
    params = {"category": "linear", "symbol": symbol}

    r = requests.get(url, params=params, timeout=15)

    # Önce HTTP status kontrol
    if r.status_code != 200:
        raise RuntimeError(f"HTTP hata: {r.status_code} - {r.text}")

    # JSON parse etmeyi dene
    try:
        data = r.json()
    except Exception:
        raise RuntimeError(f"JSON parse hatası. Gelen cevap: {r.text}")

    # API hata kontrol
    if data.get("retCode") != 0:
        raise RuntimeError(f"Bybit API hata: {data}")

    return float(data["result"]["list"][0]["lastPrice"])


def main():
    print("---- Tarama Başladı ----")
    for symbol in SYMBOLS:
        price = check_price(symbol)
        print(f"{symbol} fiyat: {price}")
    print("------------------------")


if __name__ == "__main__":
    main()
