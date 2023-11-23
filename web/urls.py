from django.urls import path 
from . import views




urlpatterns = [

       path('', views.home, name=""),
       path('register', views.register, name="register"),
       path('my-login', views.my_login, name="my-login"),
       path('user-logout', views.user_logout, name="user-logout"),
       path('dashboard',views.dashboard, name="dashboard"),
       path('creator',views.creator, name="creator"),

]