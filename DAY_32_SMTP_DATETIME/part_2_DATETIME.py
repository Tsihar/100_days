import datetime as dt

# работа с текущей датой
now = dt.datetime.now()  # dt модуль и в нем класс datetime
print(now)  # return 2025-11-03 23:23:46.590475, class = datetime.datetime

year = now.year  # атрибуты month, minute etc.
print(year)  # 2025, class = 'int'

if year == 2025:
    print("It's ok")

day_of_week = now.weekday()
print(day_of_week)  # 0, значит понедельник

# создать дату, как объект класса datetime
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)  # 1995-12-15 00:00:00, время по дефолту ставится

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)  # 1995-12-15 04:00:00
