##################### Extra Hard Starting Project ######################
import random
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas
import datetime as dt

gmail_login = "appbrewery87@gmail.com"
gmail_app_password = "rtqw vcqi bxbn ebvr"

yahoo_mail = "app_brewery@yahoo.com"

data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')
print(birthdays)

current_date = dt.datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day

for row in birthdays:
    if row['month'] == month and row['day'] == day:
        email = row['email']
        letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
        with open(random.choice(letters), mode='r') as letter:
            letter_text = letter.read()
            updated_letter = letter_text.replace('[NAME]', row['name'])
            print(updated_letter)

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=gmail_login, password=gmail_app_password)
            connection.sendmail(from_addr=gmail_login, to_addrs=email,
                                msg=f'Subject:Happy birthday!\n\n{updated_letter}')




