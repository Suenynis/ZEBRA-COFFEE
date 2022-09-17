from django.urls import path
from . import views

urlpatterns = [
    path('', views.apper,  name='New_app'),
]