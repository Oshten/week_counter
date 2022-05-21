from datetime import date as d
from datetime import timedelta as td

from django.test import TestCase

from week_counter.week_counter_app import functions

start_dates = [
    d(day=16, month=5, year=2022),
    d(day=19, month=5, year=2022),
    d(day=22, month=5, year=2022)
]
first_days_week = [0, 3, 6]

results_to_end = [[6, 2, 5], [3, 6, 2], [0, 3, 6]]
results_from_start = [[0, 4, 1], [3, 0, 4], [6, 3, 0]]

given_dates_after_or_before_start_date = [1, 3, 5, 10]

class TestClass(TestCase):
    """Класс для тестирования функций"""

    def test_remainder_to_end_week(self):
        """Проверка условия расчета остатка до конца недели"""
        for start_date, results in zip(start_dates, results_to_end):
            for first_day_week, result in zip(first_days_week, results):
                self.assertEqual(functions.calculation_end_week(start_date, first_day_week), result)

    def test_remainder_from_start_week(self):
        """Проверка условия расчета остатка от начала недели"""
        for start_date, results in zip(start_dates, results_from_start):
            for first_day_week, result in zip(first_days_week, results):
                self.assertEqual(functions.calculation_start_week(start_date, first_day_week), result)

    def test_positive_week_counter(self):
        """Проверка функции вычислителя номера недели для даты после START_DATA"""
        day = functions.START_DATE + td(days=1)
        result = 2 if day.weekday() == functions.FIRST_DAY_WEEK else 1
        self.assertEqual(functions.positive_week_counter(day), result)
        for week in given_dates_after_or_before_start_date:
            date = functions.START_DATE + td(weeks=week)
            self.assertEqual(functions.positive_week_counter(date), week+1)

    def test_negative_week_counter(self):
        """Проверка функции вычислителя номера недели для даты перед START_DATA"""
        day = functions.START_DATE - td(days=1)
        result = -1 if functions.START_DATE.weekday() == functions.FIRST_DAY_WEEK else 1
        self.assertEqual(functions.negative_week_counter(day), result)
        for weeks in given_dates_after_or_before_start_date:
            date = functions.START_DATE - td(weeks=weeks)
            self.assertEqual(functions.negative_week_counter(date), - weeks)

