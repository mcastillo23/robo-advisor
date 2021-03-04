# this is the "app/robo_advisor.py" file

import requests
import json
import os
from dotenv import load_dotenv
import csv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = input("Please input a sotck or cryptocurrency symbol.")

if symbol.isalpha() == False or len(symbol) > 5:
    print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    exit()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

response = requests.get(request_url)

if "Error Message" in response.text:
    print("Sorry, couldn't find any trading data for that stock symbol.")
    exit()

parsed_response = json.loads(response.text)

time_series = parsed_response["Time Series (Daily)"]
dates = list(time_series.keys())

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = time_series[dates[0]]["4. close"]
latest_close = time_series[dates[0]]["4. close"]

high_prices = [float(time_series[date]["2. high"]) for date in dates]
low_prices = [float(time_series[date]["3. low"]) for date in dates]

recent_high = max(high_prices)
recent_low = min(low_prices)

csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", "prices.csv") # a relative filepath

with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
    writer.writeheader() 
    for date in dates:
        writer.writerow({
            "timestamp": date, 
            "open": time_series[date]["1. open"], 
            "high": time_series[date]["2. high"], 
            "low": time_series[date]["3. low"], 
            "close": time_series[date]["4. close"], 
            "volume": time_series[date]["5. volume"]
            })
    

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {latest_close}")
print(f"RECENT HIGH: {recent_high}")
print(f"RECENT LOW: {recent_low}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


