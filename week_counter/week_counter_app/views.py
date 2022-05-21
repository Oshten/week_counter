from django import views
from django.shortcuts import render

from week_counter.week_counter_app import forms, functions
from week_counter.settings import START_DATE, FIRST_DAY_WEEK

class DateView(views.View):
    """Представление для страницы c формой ввода интересующей даты"""
    def get(self, request):
        """Обработка GET запроса"""
        data_form = forms.DateForm()
        return render(request, 'week_counter_app/date_entry_page.html', context={'data_form': data_form})

    def post(self, request):
        """Обработка POST запроса"""
        data_form = forms.DateForm(request.POST)
        if data_form.is_valid():
            date = data_form.cleaned_data['date']
            # Вычисляем номер недели
            if date > START_DATE:
                # Рассматриваем случай когда выбрана дата после START_DATA.
                week_number = functions.positive_week_counter(date)
            elif date < START_DATE:
                # Рассматриваем случай когда выбрана дата до START_DATA.
                week_number = functions.negative_week_counter(date)
            else:
                # Выбрана дата START_DATA.
                week_number = 1
            start_date = START_DATE
            first_day = functions.NAME_WEEKDAY[FIRST_DAY_WEEK]
            context = {'week_number': week_number, 'date': date, 'start_date': start_date, 'first_day': first_day}
            return render(request, 'week_counter_app/week_number_page.html', context=context)
        else:
            return render(request, 'week_counter_app/date_entry_page.html', context={'data_form': data_form})





