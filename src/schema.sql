-- Schema for Canon G7X Stock Watch
-- Stores Canon (CAJ) stock price data fetched from Alpha Vantage API

CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    price REAL NOT NULL,
    volume TEXT,
    trading_day TEXT NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
