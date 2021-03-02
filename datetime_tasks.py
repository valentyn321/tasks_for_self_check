import calendar
import pytz
from datetime import datetime as dt
from datetime import date


year = 2021


def today_to_str():
    s1 = dt.today().strftime("%d-%m-%Y")
    s2 = dt.today().strftime("%d %b, %A %y")
    s3 = dt.today().strftime("%d %B %Y")
    return s1, s2, s3


def str_to_datetime(string_tuple):
    dt1 = dt.strptime(string_tuple[0], "%d-%m-%Y")
    dt2 = dt.strptime(string_tuple[1], "%d %b, %A %y")
    dt3 = dt.strptime(string_tuple[2], "%d %B %Y")
    return dt1, dt2, dt3


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


def difference(tz1, tz2):
    first_tz = pytz.timezone(tz1)
    second_tz = pytz.timezone(tz2)

    first_dt = first_tz.localize(dt(2000, 1, 24, 12, 35))
    second_dt = second_tz.localize(dt(2000, 1, 25, 18, 35))

    elapsedTime = second_dt - first_dt
    return elapsedTime
