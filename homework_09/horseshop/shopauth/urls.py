from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import shopauth.views as shopauth

app_name = 'shopauth'

urlpatterns = [
    path('register/',shopauth.ShopUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]