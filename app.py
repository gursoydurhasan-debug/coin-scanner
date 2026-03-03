import requests
import time

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]  # <-- burası önemli

def check_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price"
    r = requests.get(url, params={"symbol": symbol}, timeout=10)
    data = r.json()

    # Hata döndüyse (invalid symbol vs.)
    if "price" not in data:
        raise RuntimeError(f"{symbol} için Binance cevap hatası: {data}")

    return float(data["price"])


def main():
    print("---- Tarama Başladı ----")
    for symbol in SYMBOLS:
        price = check_price(symbol)
        print(f"{symbol} fiyat: {price}")
    print("------------------------")


if __name__ == "__main__":
    # GitHub Actions'ta sonsuz döngü istemiyoruz. 1 kere çalışsın.
    main()
