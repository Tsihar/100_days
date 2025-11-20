import datetime
from pprint import pprint

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = "z9VPIZQM0K56SK4COz"
FUNCTION_DAILY = "TIME_SERIES_DAILY"

params = {
    "function": FUNCTION_DAILY,
    "apikey": STOCK_API_KEY,
    "symbol": STOCK
}

response = requests.get(url=STOCK_URL, params=params)
response.raise_for_status()
data = response.json()
pprint(data)

today = datetime.datetime.now()
today_date = str(today.date() - datetime.timedelta(days=2))
yesterday_date = str(today.date() - datetime.timedelta(days=10))
print(today_date)
print(yesterday_date)

close_price_today = float(data['Time Series (Daily)'][today_date]['4. close'])
close_price_yesterday = float(data['Time Series (Daily)'][yesterday_date]['4. close'])
print(close_price_today)
print(close_price_yesterday)
curr_deviation = ((close_price_today - close_price_yesterday)/close_price_yesterday)*100
deviation_5 = (close_price_yesterday * 5)/100

if close_price_today > close_price_yesterday + deviation_5:
    print(f"Get News. TSLA raises by {round(curr_deviation, 2)}")

elif close_price_today < close_price_yesterday - deviation_5:
    print(f"Get News: TSLA lost {round(abs(curr_deviation), 2)}")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

