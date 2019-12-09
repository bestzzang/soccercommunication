from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'member'

urlpatterns = [
    path('profile_update/', login_required(ProfileUpdateView.as_view()), name='profile_update'),
    path('profile/<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
    path('profile_delete/', login_required(profile_delete), name='profile_delete'),
    path('password/', login_required(change_password), name='change_pw'),
]
