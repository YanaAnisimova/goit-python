from datetime import datetime, timedelta


def get_days_from_today(date):

    date = date.split('-')
    date = datetime(year=int(date[0]), month=int(
        date[1]), day=int(date[2])).date()
    current_date = datetime.now().date()
    delta = (current_date - date).days

    return delta


print(get_days_from_today('2021-10-09'))
