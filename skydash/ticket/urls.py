from django.urls import path

from ticket import views

app_name = 'ticket'

urlpatterns = [
    path('create/', views.createTicket, name='create'),
    path('update/<str:pk>/', views.updateTicket, name='update'),
    path('delete/<str:pk>/', views.deleteTicket, name='delete'),
]
