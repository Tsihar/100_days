import datetime as dt
import random
import smtplib


gmail_login = "appbrewery87@gmail.com"
gmail_password = "746681app"
gmail_app_password = "rtqw vcqi bxbn ebvr"

yahoo_mail = "app_brewery@yahoo.com"
yahoo_password = "7789987798"

current_weekday = dt.datetime.now().weekday()

if current_weekday == 1:
    with open(file="quotes.txt", mode="r") as file:
        quotes = file.readlines()
        rand_quote = random.choice(quotes)
        print(rand_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=gmail_login, password=gmail_app_password)
        connection.sendmail(from_addr=gmail_login, to_addrs=yahoo_mail,
                            msg=f"Subject:Happy Birthday!\n\n{rand_quote}")
