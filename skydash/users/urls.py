from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.loginForMentor, name='login'),
    path('logout/', views.logoutMentor, name='logout'),

    path('register/', views.register, name='register'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete')
]
