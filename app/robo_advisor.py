# this is the "app/robo_advisor.py" file

import requests
import json
import os
from dotenv import load_dotenv
import csv
from datetime import datetime
from pandas import read_csv
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

#Function to format output in USD
def to_usd(my_price):
    return f"${my_price:,.2f}" 

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
symbol = input("Please input a stock or cryptocurrency symbol.")

#Validating ticker input
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

#Reading the stock's prices into variables
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = time_series[dates[0]]["4. close"]
latest_close = time_series[dates[0]]["4. close"]

high_prices = [float(time_series[date]["2. high"]) for date in dates]
low_prices = [float(time_series[date]["3. low"]) for date in dates]

recent_high = max(high_prices)
recent_low = min(low_prices)

#Creating a CSV file with past prices
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

#Recommendation algorithm
recommendation = "Don't Buy"
reason = "The stock's latest closing price is more than 30% above its recent low."

if float(latest_close) <= (1.3 * recent_low):
    recommendation = "Buy"
    reason = "The stock's latest closing price is less than or equal to 30% above its recent low."

#Command-line output
print("-------------------------")
print(f"SELECTED SYMBOL: {symbol.upper()}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", datetime.now().strftime("%Y-%m-%d %I:%M %p"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(recent_high)}")
print(f"RECENT LOW: {to_usd(recent_low)}")
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}!")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#Creating a line plot of price over time
prices_df = read_csv(csv_file_path)
prices_df.sort_values(by="timestamp", ascending=True, inplace=True)

price_plot = sns.lineplot(data = prices_df, x = "timestamp", y = "close")
price_plot.set(xlabel ='Date', ylabel ='Closing Price($)', title = f'{symbol.upper()} Closing Price Over Time')
plt.xticks(rotation = 45, ha = 'right', fontsize = 5)
plt.show()