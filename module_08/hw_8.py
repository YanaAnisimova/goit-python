from collections import defaultdict
from datetime import datetime, timedelta


users = [
    {'name': 'Anna', 'birthday': datetime(year=1991, month=5, day=12)},
    {'name': 'Vova', 'birthday': datetime(year=1992, month=5, day=16)},
    {'name': 'Masha', 'birthday': datetime(year=1993, month=5, day=6)},
    {'name': 'Dasha', 'birthday': datetime(year=1994, month=5, day=20)},
    {'name': 'Sonya', 'birthday': datetime(year=1995, month=5, day=17)},
    {'name': 'Roma', 'birthday': datetime(year=1996, month=5, day=19)},
    {'name': 'Katya', 'birthday': datetime(year=1997, month=5, day=22)},
]


def congratulate(birthday_list):

    for weekday in birthday_list:
        print(f'{weekday}: {", ".join(birthday_list[weekday])}\n')


def making_a_birthday_list(users, start_date):

    birthday_list = defaultdict(list)

    for j in [start_date + timedelta(i) for i in range(7)]:
        for user in users:
            current_birthday = user['birthday'].replace(
                year=datetime.now().year)
            if j.date() == current_birthday.date():
                weekday_birthday = current_birthday.strftime("%A")
                if weekday_birthday in ('Saturday', 'Sunday'):
                    weekday_birthday = 'Monday'
                birthday_list[weekday_birthday].append(user["name"])
    return birthday_list


def starting_date_definition():

    current_date = datetime.now()

    if current_date.weekday() == 0:
        delta = timedelta(days=2)
        start_date = current_date - delta
    else:
        delta = timedelta(days=5 - current_date.weekday())
        start_date = current_date + delta

    return start_date


def main():
    start_date = starting_date_definition()
    birthday_list = making_a_birthday_list(users, start_date)
    congratulate(birthday_list)


if __name__ == '__main__':
    main()
