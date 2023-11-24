from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [

       path('', views.home, name=""),

       # - Authentication

       path('register', views.register, name="register"),
       path('my-login', views.my_login, name="my-login"),
       path('user-logout', views.user_logout, name="user-logout"),


       # - CRUD

       path('dashboard',views.dashboard, name="dashboard"),
       path('create-record', views.create_record, name="create-record"),
       path('update-record/<int:pk>', views.update_record, name='update-record'),
       path('record/<int:pk>', views.singular_record, name="record"),
       path('delete-record/<int:pk>', views.delete_record, name="delete-record"),


       # - Developer/Creator
       path('developer',views.creator, name="developer"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)