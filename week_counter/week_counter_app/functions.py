import datetime

from week_counter.settings import START_DATE, FIRST_DAY_WEEK


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

def calculation_end_week(start_date: datetime.date, first_day_week: int) -> int:
    """Вычислим остаток первой недели до окончания"""
    if start_date.weekday() < first_day_week:
        remainder_to_end_week = 6 - start_date.weekday() - (7 - first_day_week)
    else:
        remainder_to_end_week = 6 - start_date.weekday() + first_day_week
    return remainder_to_end_week

def calculation_start_week(start_date: datetime.date, first_day_week: int) -> int:
    """Вычислим остаток первой недели от начала"""
    if start_date.weekday() < first_day_week:
        remainder_from_start_week = (7 - first_day_week) + start_date.weekday()
    else:
        remainder_from_start_week = start_date.weekday() - first_day_week
    return remainder_from_start_week

def positive_week_counter(date: datetime.date) -> int:
    """Вычислитель номера недели для даты после START_DATA"""
    days_count = (date - START_DATE).days
    remainder_to_end_week = calculation_end_week(START_DATE, FIRST_DAY_WEEK)
    full_weeks_number = (days_count - remainder_to_end_week) // 7
    end_week_number_day = (days_count - remainder_to_end_week) % 7
    if end_week_number_day == 0:
        week_number = 1 + full_weeks_number
    else:
        week_number = 2 + full_weeks_number
    return week_number

def negative_week_counter(date)  -> int:
    """Вычислитель номера для даты до START_DATA"""
    days_count = (START_DATE - date).days
    remainder_from_start_week = calculation_start_week(START_DATE, FIRST_DAY_WEEK)
    full_weeks_number = (days_count - remainder_from_start_week) // 7
    end_week_number_day = (days_count - remainder_from_start_week) % 7
    if full_weeks_number == -1 or days_count == remainder_from_start_week:
        week_number = 1
    elif full_weeks_number == 0:
        week_number = -1
    elif end_week_number_day == 0:
        week_number = - full_weeks_number
    else:
        week_number = - full_weeks_number - 1
    return week_number
