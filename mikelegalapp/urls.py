from django.urls import path
from .views import add_subscriber, unsubscribe

urlpatterns = [
    path('add_subscriber/', add_subscriber, name='add_subscriber'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
]