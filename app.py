import requests

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

def check_price(symbol):
    url = "https://fapi.binance.com/fapi/v1/ticker/price"
    params = {"symbol": symbol}

    r = requests.get(url, params=params, timeout=15)

    if r.status_code != 200:
        raise RuntimeError(f"HTTP hata: {r.status_code} - {r.text}")

    data = r.json()

    return float(data["price"])


def main():
    print("---- Tarama Başladı ----")
    for symbol in SYMBOLS:
        price = check_price(symbol)
        print(f"{symbol} fiyat: {price}")
    print("------------------------")


if __name__ == "__main__":
    main()
