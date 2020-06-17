from django.urls import path

from user_account.views import CreateUserAccountView, UserAccountLoginView, UserAccountLogoutView, \
    user_account_update_profile

urlpatterns = [

    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', user_account_update_profile, name='profile'),
]
