from django.conf.urls import url
from django.urls import path, include
from dapp import views
app_name = 'dapp'

urlpatterns=[
    path('register_org/',views.register_org,name='register_org'),
    path('user_login/',views.user_login,name='user_login'),
    path('register_user/', views.register_user, name='register_user'),
]