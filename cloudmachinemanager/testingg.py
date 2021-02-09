import datetime


def Give_current_weekday():
    weekday = datetime.date.today().strftime("%A")
    return weekday
print(Give_current_weekday())
