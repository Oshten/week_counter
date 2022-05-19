from django.urls import path

from week_counter.week_counter_app import views

urlpatterns = [
    path('', views.DateView.as_view(), name='date_entry_page'),
]