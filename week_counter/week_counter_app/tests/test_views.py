from django.test import TestCase
from django.urls import reverse

from datetime import date



class TestClass(TestCase):
    """Класс для тестирования представлений"""

    def test_get_dateview(self):
        """Проверка запроса get"""
        url = reverse('date_entry_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'week_counter_app/date_entry_page.html')

    def test_post_dateview(self):
        """Проверка запроса post"""
        url = reverse('date_entry_page')
        day = date(day=16, month=5, year=2022)
        start_day = date(day=1, month=5, year=2022)
        context = {'week_number': 10, 'date': day, 'start_date': start_day, 'first_day': 'test'}
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'week_counter_app/date_entry_page.html')
        response = self.client.post(url, context)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'week_counter_app/week_number_page.html')