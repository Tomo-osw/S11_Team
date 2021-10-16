from django.urls import path
from . import views

app_name = 'myhp'
urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('homemap', views.homemap, name='homemap'),
    path('makepost', views.makepost, name='makepost'),
    path('index2', views.index2, name='index2'),
    path('indexwhenplacenametapped', views.indexwhenplacenametapped, name='indexwhenplacenametapped'),
=======
    path('', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('register/', views.AccountRegistration.as_view(), name='register'),
    path('home/', views.home, name='home'),
>>>>>>> 5162d33b671c50f08ca518c54c952febd5305850
]