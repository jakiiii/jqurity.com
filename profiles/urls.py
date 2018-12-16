from django.urls import path

from .views import (
    ProfileView,
    UserInfoUpdateView,
    UserPostListView,
    UserPostCreateView,
    UserPostUpdateView,
    UserPostDeleteView
)


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('posts/', UserPostListView.as_view(), name='user-post'),
    path('update/', UserInfoUpdateView.as_view(), name='update-info'),
    path('create/', UserPostCreateView.as_view(), name='create-post'),
    path('update/<slug:slug>/', UserPostUpdateView.as_view(), name='update-post'),
    path('delete/<slug:slug>/', UserPostDeleteView.as_view(), name='delete'),
]
