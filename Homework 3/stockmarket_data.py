"""
# Author: Isaac Jarrells
# Date: Feburary 6, 2025
# File: stockmarket_data.py
# Purpose: To fetch online stock prices and produce certain calculations.
# Resources: Use ChatGPT to figure out the header situation and how to implement it which in turn
#            allowed me to get passed robot.txt problem.
# Version 1.0: Initial Retrival of Data
"""

import requests
from requests import get
from datetime import date
from json import loads
from urllib3.exceptions import HTTPError

"""Download data retrieves online data from Nasdaq on a ticker set by the user and return the dictionary of values"""
def download_data(ticker: str) -> dict:
    today = date.today()  # initializes date as today from the time library.
    base_url = "https://api.nasdaq.com"
    start = str(today.replace(year=today.year - 5))
    path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
    url = f"{base_url}{path}"

    """Headers is the need to pass by bot blocking that Nasdaq uses."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    print(f"Fetching {ticker} stock prices from {start} to {today}...")

    try:
        """Fetches URL and times out the request attempt if suppasses 5 seconds"""
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status() # print check for error during HTTP process
        return response.json()
    except HTTPError as e: # if HTTP fetch requests produces an error
        print(f"HTTPError: {e.code} - {e.reason}")
    except Exception as e: # if the code produces an error such as undefined libraries
        print(f"Error: {e}")

ticker = "AAPL" # AAPL is hardcoded ticker until user input is accepted
ticker = ticker.upper() # set the tick to all upper case letters
print(download_data(ticker)) # prints the dict of data from Nasdaq