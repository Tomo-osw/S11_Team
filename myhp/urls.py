from django.urls import path
from . import views

app_name = 'myhp'
urlpatterns = [
    path('', views.index, name='index'),
    path('homemap', views.homemap, name='homemap'),
    path('post', views.post, name='post'),
    path('index2', views.index2, name='index2'),
]