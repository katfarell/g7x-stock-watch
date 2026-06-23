import requests
from database import setup_database, save_stock_price

API_KEY = "6EUQFPEZFN9UHANH"
SYMBOL = "CAJ"  # Canon Inc. on NYSE

def fetch_and_store():
    """Fetch Canon stock data from Alpha Vantage and store it in the database."""

    # Set up database tables
    setup_database()

    # Fetch latest stock quote from Alpha Vantage
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": SYMBOL,
        "apikey": API_KEY,
    }

    print(f"Fetching stock data for {SYMBOL}...")
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    quote = data.get("Global Quote", {})

    if not quote:
        print("No data returned from API. Check your API key or symbol.")
        return

    symbol = quote["01. symbol"]
    price = float(quote["05. price"])
    volume = quote["06. volume"]
    trading_day = quote["07. latest trading day"]

    # Store in database
    save_stock_price(symbol, price, volume, trading_day)
    print("Done!")


if __name__ == "__main__":
    fetch_and_store()
