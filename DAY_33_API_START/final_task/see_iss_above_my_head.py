import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 53.904541  # Your latitude
MY_LONG = 27.561523  # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.
def iss_is_in_my_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_lat_equals_mine = MY_LAT - 5 < iss_latitude < MY_LAT + 5
    iss_lng_equals_mine = MY_LONG - 5 < iss_longitude < MY_LONG + 5
    return iss_lat_equals_mine, iss_lng_equals_mine


def get_current_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Europe/Minsk"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().astimezone()
    actual_hour = time_now.hour
    print(time_now)

    return sunset < actual_hour and actual_hour > sunrise
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(5)
    iss = iss_is_in_my_location()
    print(iss)
    if all(iss):
        cur_time = get_current_time()
        print(cur_time)
        if cur_time:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user="appbrewery87@gmail.com", password="rtqw vcqi bxbn ebvr")
                connection.sendmail(from_addr="appbrewery87@gmail.com",
                                    to_addrs="app_brewery@yahoo.com",
                                    msg="Subject:See the iss\n\nIt's currently above your head")
    time.sleep(5)


