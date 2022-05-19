import datetime

from week_counter.settings import START_DATA, FIRST_DAY_WEEK


#Название дней недели
NAME_WEEKDAY = {
    0: 'понедельник',
    1: 'вторник',
    2: 'среда',
    3: 'четверг',
    4: 'пятница',
    5: 'суббота',
    6: 'воскресенье',
}

#Вычислим остаток первой недели до окончания и остаток первой недели от начала
if START_DATA.day < FIRST_DAY_WEEK:
    REMAINDER_TO_END_FIRST_WEEK = 6 - START_DATA.day - (7 - FIRST_DAY_WEEK)
    REMAINDER_FROM_START_FIRST_WEEK = (7 - FIRST_DAY_WEEK) + START_DATA.day
else:
    REMAINDER_TO_END_FIRST_WEEK = 6 - START_DATA.day + FIRST_DAY_WEEK
    REMAINDER_FROM_START_FIRST_WEEK = 7 - FIRST_DAY_WEEK - (6 - START_DATA.day)


def positive_week_counter(date: datetime.date) -> int:
    """Вычислитель номера недели для даты после START_DATA"""
    days_count = (date - START_DATA).days
    full_weeks_number = (days_count - REMAINDER_TO_END_FIRST_WEEK) // 7
    end_week_number_day = (days_count - REMAINDER_TO_END_FIRST_WEEK) % 7
    if end_week_number_day == 0:
        week_number = 1 + full_weeks_number
    else:
        week_number = 2 + full_weeks_number
    return week_number

def negative_week_counter(date)  -> int:
    """Вычислитель номера для даты до START_DATA"""
    days_count = (START_DATA - date).days
    full_weeks_number = (days_count - REMAINDER_FROM_START_FIRST_WEEK) // 7
    end_week_number_day = (days_count - REMAINDER_FROM_START_FIRST_WEEK) % 7
    if end_week_number_day == 0:
        week_number = -full_weeks_number
    else:
        week_number = -full_weeks_number - 1
    return week_number

