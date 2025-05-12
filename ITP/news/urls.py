from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_home, name='new_home'),
]