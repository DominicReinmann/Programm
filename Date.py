import datetime

# Get the current date


class Date:
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%y")
    print(day + '.' + month + '.' + year)
