# this is the "app/robo_advisor.py" file

import requests
import json

symbol = input("Please input a sotck or cryptocurrency symbol.")

if symbol.isalpha() == False or len(symbol) > 5:
    print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    exit()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

response = requests.get(request_url)
print(type(response))
print(response.status_code)

parsed_response = json.loads(response.text)
print(type(parsed_response))

#print("-------------------------")
#print("SELECTED SYMBOL: XYZ")
#print("-------------------------")
#print("REQUESTING STOCK MARKET DATA...")
#print("REQUEST AT: 2018-02-20 02:00pm")
#print("-------------------------")
#print("LATEST DAY: 2018-02-20")
#print("LATEST CLOSE: $100,000.00")
#print("RECENT HIGH: $101,000.00")
#print("RECENT LOW: $99,000.00")
#print("-------------------------")
#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")