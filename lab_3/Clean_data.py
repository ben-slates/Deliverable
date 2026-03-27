
import yfinance as yf
import pandas as pd

def fetch_and_clean_stock_data(ticker, start_date, end_date, output_file):
    """Fetches stock data and cleans it to a simple CSV format."""
    try:
        # Download the data
        df = yf.download(ticker, start=start_date, end=end_date)
        
        # yfinance now returns a multi-index for columns if only one ticker is requested
        # We want to flatten this and just keep the 'Close', 'Open', etc. columns
        if isinstance(df.columns, pd.MultiIndex):
            # For a single ticker, levels are usually (Metric, Ticker)
            # We'll just keep the Metric level
            df.columns = df.columns.get_level_values(0)
            
        # Ensure the index is named 'Date'
        df.index.name = 'Date'
        
        # Save to CSV
        df.to_csv(output_file)
        print(f"Successfully fetched and cleaned {ticker} data and saved to {output_file}")
        print("CSV Header:")
        print(df.head())
    except Exception as e:
        print(f"Error fetching and cleaning data for {ticker}: {e}")

if __name__ == "__main__":
    fetch_and_clean_stock_data("AAPL", "2019-01-01", "2024-01-01", "numpy_stock_analysis/AAPL_stock_data.csv")
