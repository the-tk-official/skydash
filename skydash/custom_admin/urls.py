from django.urls import path

from custom_admin import views

urlpatterns = [
    path('users/', views.accounts, name='accounts'),
    path('courses/', views.courses, name='courses'),
    path('tickets/', views.tickets, name='tickets')
]
