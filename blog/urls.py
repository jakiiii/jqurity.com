from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail')
]
