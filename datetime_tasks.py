import calendar
from datetime import datetime as dt
from datetime import date


s1 = dt.today().strftime("%d-%m-%Y")
s2 = dt.today().strftime("%d %b, %A %y")
s3 = dt.today().strftime("%d %B %Y")
# print(s1, s2, s3)

dt1 = dt.strptime(s1, "%d-%m-%Y")
dt2 = dt.strptime(s2, "%d %b, %A %y")
dt3 = dt.strptime(s3, "%d %B %Y")
# print(dt1, dt2, dt3)

year = 2021


def sundays_finder(year):
    sundays = []
    my_calendar = calendar.TextCalendar(calendar.SUNDAY)
    for month in range(1, 13):
        for day_date in my_calendar.itermonthdays(year, month):
            if day_date != 0:
                day = date(year, month, day_date)
                if day.weekday() == 6:
                    sundays.append("%d-%d" % (day_date, month))
    return sundays


def workdays_finder(year):
    workdays = 0
    my_calendar = calendar.TextCalendar()
    for month in range(1, 13):
        for day_date in my_calendar.itermonthdays(year, month):
            if day_date != 0:
                day = date(year, month, day_date)
                if day.weekday() < 5:
                    workdays += 1
    return workdays


print(sundays_finder(year))