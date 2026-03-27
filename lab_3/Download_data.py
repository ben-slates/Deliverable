
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date, output_file):
    """Fetches stock data for a given ticker and saves it to a CSV file."""
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if not stock_data.empty:
            stock_data.to_csv(output_file)
            print(f"Successfully fetched {ticker} data and saved to {output_file}")
        else:
            print(f"No data found for {ticker} between {start_date} and {end_date}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

if __name__ == "__main__":
    # Example usage:
    # Fetch Apple stock data for the last 5 years
    fetch_stock_data("AAPL", "2019-01-01", "2024-01-01", "numpy_stock_analysis/AAPL_stock_data.csv")
    # You can add more tickers here if needed
    # fetch_stock_data("MSFT", "2019-01-01", "2024-01-01", "numpy_stock_analysis/MSFT_stock_data.csv")
