from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_new, name='place_new'),
    path('post/list', views.place_list, name='place_list'),
]