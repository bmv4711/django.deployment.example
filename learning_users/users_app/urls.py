#from django.conf.urls import url
from users_app import views
from django.urls import path
# Template urls
app_name = 'users_app'

urlpatterns = [
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
