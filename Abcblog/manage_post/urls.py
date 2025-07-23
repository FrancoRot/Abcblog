from django.urls import path
from .views import IndexView

urlpatterns = [
    path('manage/', IndexView.as_view(), name='manage_index'),
]
