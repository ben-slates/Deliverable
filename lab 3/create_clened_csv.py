
import pandas as pd

def clean_stock_data(input_file, output_file):
    """Cleans the CSV data from yfinance to handle multi-level headers."""
    try:
        # Load the CSV skipping the first few rows that are not data
        df = pd.read_csv(input_file, header=[0, 1, 2], index_col=0)
        
        # Simplify the multi-level index (columns)
        # The columns are like ('Price', 'Close', 'AAPL')
        # We want to keep just the second level ('Close')
        df.columns = df.columns.get_level_values(1)
        
        # Ensure the index is named 'Date'
        df.index.name = 'Date'
        
        # Save the cleaned data
        df.to_csv(output_file)
        print(f"Successfully cleaned data and saved to {output_file}")
    except Exception as e:
        print(f"Error cleaning data: {e}")

if __name__ == "__main__":
    clean_stock_data("numpy_stock_analysis/AAPL_stock_data.csv", "numpy_stock_analysis/AAPL_stock_data_cleaned.csv")
