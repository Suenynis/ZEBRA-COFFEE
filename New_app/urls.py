from django.urls import path
from . import views

urlpatterns = [
    path('', views.apper, name='New_app'),
    path('about/', views.Home.as_view()),
    path('registration/', views.Userform.as_view())
]