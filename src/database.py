import sqlite3

DB_PATH = "stock_watch.db"


def get_connection():
    """Connect to the SQLite database and return the connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def setup_database():
    """Run schema.sql to create tables if they don't exist."""
    conn = get_connection()
    with open("src/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database ready.")


def save_stock_price(symbol, price, volume, trading_day):
    """Insert a stock price record into the database."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO stock_prices (symbol, price, volume, trading_day) VALUES (?, ?, ?, ?)",
        (symbol, price, volume, trading_day),
    )
    conn.commit()
    conn.close()
    print(f"Saved: {symbol} ${price} on {trading_day}")
