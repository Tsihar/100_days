import datetime
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from pprint import pprint

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = "9VPIZQM0K56SK4CO"
FUNCTION_DAILY = "TIME_SERIES_DAILY"

params_stock = {
    "function": FUNCTION_DAILY,
    "apikey": STOCK_API_KEY,
    "symbol": STOCK
}

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "89030e29862f4a80818467204c3fdc1f"

params_news = {
    "q": "TESLA",
    "apiKey": NEWS_API_KEY,
    "sortBy": "publishedAt",
    "pageSize": 3
}


def get_news():
    response_news = requests.get(url=NEWS_URL, params=params_news)
    response_news.raise_for_status()
    data_news = response_news.json()
    pprint(data_news)
    all_news = ""
    for i, news in enumerate(data_news['articles']):
        print(f"{i+1}. {news['title']}")
        all_news += f"{news['title']}\n{news['content']}\n\n"

    return all_news

def send_email(increase, percentage, text):
    body = f"{text}"

    msg = MIMEText(body, "plain", "utf-8")

    # === Кодируем заголовки ===
    msg["Subject"] = Header(f"{increase} {percentage}%", "utf-8")
    msg["From"] = Header("appbrewery87@gmail.com", "utf-8")
    msg["To"] = Header("gomailowner@gmail.com", "utf-8")

    # Письмо должно быть передано как bytes
    raw_message = msg.as_bytes()

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="appbrewery87@gmail.com", password="rtqw vcqi bxbn ebvr")
        connection.sendmail(from_addr="appbrewery87@gmail.com",
                            to_addrs="gomailowner@gmail.com",
                            msg=raw_message)


response = requests.get(url=STOCK_URL, params=params_stock)
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
    got_news = get_news()
    send_email("🔺", round(curr_deviation, 2), got_news)

elif close_price_today < close_price_yesterday - deviation_5:
    print(f"Get News: TSLA lost {round(abs(curr_deviation), 2)}")
    got_news = get_news()
    send_email("🔻", round(abs(curr_deviation), 2), got_news)

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

