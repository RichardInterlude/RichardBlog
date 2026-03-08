from . views import RegisterationView, LoginView, LogoutView, ProfileView, DeleteUserView
from django.urls import path, include


urlpatterns = [
    path('register/', RegisterationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
]

