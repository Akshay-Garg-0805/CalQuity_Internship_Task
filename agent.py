import subprocess
import json
import re
from tools.finance_tool import get_stock_price, fetch_and_plot_stock_trend
import datetime

def load_model(prompt):
    llama_bin = "./llama.cpp/build/bin/llama-run"
    model_path = "file://./models/mistral-7b-instruct-v0.1.Q6_K.gguf" 

    result = subprocess.run([llama_bin, model_path, prompt], capture_output=True, text=True)
    
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    
    return result.stdout

def plot_stock_trend(stock_symbol, start_date, end_date):
    """Fetch historical data for the given range and save it as a plot."""
    
    # Define a file path to save the plot (e.g., in the current directory)
    file_path = f"{stock_symbol}_stock_trend_{start_date}_to_{end_date}.png"
    
    # Fetch the historical data and save the plot
    plot_result = fetch_and_plot_stock_trend(stock_symbol, start_date, end_date, file_path)
    return plot_result  # Return the result of plotting

def financial_agent(user_input):
    
    # Regex for asking about the stock price (current day)
    stock_pattern = re.compile(r"what is the stock price of (\w+)", re.IGNORECASE)
    
    # Regex for asking to plot stock prices over a range (from A to B)
    plot_pattern = re.compile(r"plot stock price of (\w+) from (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})", re.IGNORECASE)
    
    # If the query asks for the stock price for the current day
    match = stock_pattern.search(user_input)
    if match:
        stock_symbol = match.group(1).upper()  # Extract stock symbol
        print(f"Fetching stock price for {stock_symbol}...")

        # Get the stock data for the current day
        stock_data = get_stock_price(stock_symbol)

        if isinstance(stock_data, dict):
            # Return stock data as text
            return f"Stock data for {stock_symbol}: {json.dumps(stock_data, indent=2)}"
        else:
            return stock_data  # If there was an error fetching stock data
    
    # If the query asks for a stock price plot for a date range
    plot_match = plot_pattern.search(user_input)
    if plot_match:
        stock_symbol = plot_match.group(1).upper()  # Extract stock symbol
        start_date = plot_match.group(2)  # Extract start date
        end_date = plot_match.group(3)  # Extract end date
        
        print(f"Fetching and saving plot for {stock_symbol} from {start_date} to {end_date}...")

        # Generate and save the plot
        plot_result = plot_stock_trend(stock_symbol, start_date, end_date)
        return plot_result  # Return the result of saving the plot
    
    else:
        # If the query is not related to finance, process it like a regular query
        print(f"Processing non-finance query: {user_input}")
        response = load_model(user_input)
        return response
