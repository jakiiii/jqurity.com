from django.urls import path
from .views import SearchListView


urlpatterns = [
    path('search/', SearchListView.as_view(), name='query'),
]
