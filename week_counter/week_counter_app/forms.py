from django import forms


class DateForm(forms.Form):
    """Форма для ввода даты"""
    date = forms.DateField(help_text='Введите дату в формате ДД.ММ.ГГГГ')