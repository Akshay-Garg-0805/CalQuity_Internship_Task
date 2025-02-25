import yfinance as yf
import matplotlib.pyplot as plt
import logging
import os

# Configure logging
logging.basicConfig(filename='financial_agent.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_stock_price(stock_symbol: str):
    """Fetch the latest stock price data for a given symbol."""
    try:
        # Fetch stock data for the given symbol
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="1d")  # Get the latest data
        
        # Return relevant stock info (convert np.float64 to regular float)
        if not data.empty:
            latest_data = data.iloc[-1]
            stock_info = {
                "Open": latest_data["Open"].item(),
                "High": latest_data["High"].item(),
                "Low": latest_data["Low"].item(),
                "Close": latest_data["Close"].item(),
                "Volume": int(latest_data["Volume"])
            }
            logging.info(f"Fetched stock data for {stock_symbol}: {stock_info}")
            return stock_info
        else:
            error_message = f"No data found for symbol {stock_symbol}"
            logging.error(error_message)
            return f"Error: {error_message}"
    
    except Exception as e:
        error_message = f"An error occurred while fetching data for {stock_symbol}: {str(e)}"
        logging.error(error_message)
        return f"Error: {error_message}"

def save_stock_plot(stock_symbol: str, data, file_path: str):
    """Save the stock data plot as an image file."""
    try:
        # Ensure we have data to plot
        if data.empty:
            logging.error(f"No data available to plot for {stock_symbol}")
            return "Error: No data available to plot"

        # Plotting the stock price data
        data['Close'].plot(title=f"{stock_symbol} Stock Price", xlabel="Date", ylabel="Price (USD)")
        
        # Save the plot as an image file
        plt.savefig(file_path)
        plt.close()  # Close the plot to avoid display
        logging.info(f"Saved stock data plot for {stock_symbol} to {file_path}")
        return f"Plot saved to {file_path}"
    except Exception as e:
        logging.error(f"Error while saving plot for {stock_symbol}: {str(e)}")
        return f"Error: {str(e)}"

def get_historical_data(stock_symbol: str, start_date: str, end_date: str):
    """Fetch historical stock data for a given period."""
    try:
        # Fetch historical data for the given period
        stock = yf.Ticker(stock_symbol)
        historical_data = stock.history(start=start_date, end=end_date)
        
        if not historical_data.empty:
            logging.info(f"Fetched historical data for {stock_symbol} from {start_date} to {end_date}")
            return historical_data
        else:
            error_message = f"No historical data found for symbol {stock_symbol} in the specified period"
            logging.error(error_message)
            return f"Error: {error_message}"
    
    except Exception as e:
        error_message = f"An error occurred while fetching historical data for {stock_symbol}: {str(e)}"
        logging.error(error_message)
        return f"Error: {error_message}"

def fetch_and_plot_stock_trend(stock_symbol: str, start_date: str, end_date: str, save_path: str):
    """Fetch historical data for a given stock and save the plot."""
    # Get historical data
    historical_data = get_historical_data(stock_symbol, start_date, end_date)
    
    if isinstance(historical_data, str):  # Error handling for failed fetch
        return historical_data
    
    # Save the plot
    return save_stock_plot(stock_symbol, historical_data, save_path)
