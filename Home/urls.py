
# home/urls.py


# home/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('driver_home/', views.driver_home, name='driver_home'),
    path('driver_profile01/', views.driver_profile, name='driver_profile01'),
    path('driver_wallet/', views.driver_wallet, name='driver_wallet'),
    
    
]
