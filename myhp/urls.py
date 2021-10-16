from django.urls import path
from . import views

app_name = 'myhp'
urlpatterns = [
    path('', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('register/', views.AccountRegistration.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('makelist/', views.makelist, name='makelist'),
    path('makepost/', views.makepost, name='makepost')
]
