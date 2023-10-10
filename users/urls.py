from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, verification_user, \
    verification_user_1, UserListView, toggle_activity

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('user/', UserListView.as_view(), name='user'),
    path('genpassword/', generate_new_password),
    path('verification/', verification_user),
    path('verification_1/', verification_user_1, name='verifications_1'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]