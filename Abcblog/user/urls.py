from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('add/', views.SingUpView.as_view(), name='register'),
]
