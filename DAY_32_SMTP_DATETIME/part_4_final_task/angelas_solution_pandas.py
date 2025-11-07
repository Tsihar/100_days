##################### Extra Hard Starting Project ######################
import random
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas
import datetime as dt

from DAY_32_SMTP_DATETIME.part_4_final_task.my_solution import birthdays

gmail_login = "appbrewery87@gmail.com"
gmail_app_password = "rtqw vcqi bxbn ebvr"

yahoo_mail = "app_brewery@yahoo.com"

data = pandas.read_csv('birthdays.csv')

current_date = dt.datetime.now()
today_month = current_date.month
today_day = current_date.day
#
# for (index, data_row) in data.iterrows():
#     i = index
#     d = data_row

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)
month_day = (today_month, today_day)

if month_day in birthdays_dict:
    birthday_man = birthdays_dict[month_day]
    with open(f"letter_{random.choice(range(1, 4))}.txt", mode='r') as letter:
        letter_text = letter.read()
        updated_letter = letter_text.replace('[NAME]', birthday_man['name'])
        print(updated_letter)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=gmail_login, password=gmail_app_password)
        connection.sendmail(from_addr=gmail_login, to_addrs=birthday_man["email"],
                            msg=f'Subject:Happy birthday!\n\n{updated_letter}')




