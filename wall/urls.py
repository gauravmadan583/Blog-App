from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='wall-home'),
    path('about', views.about, name='wall-about'),
]