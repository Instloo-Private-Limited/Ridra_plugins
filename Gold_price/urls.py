from django.urls import path 
from . import views
urlpatterns = [
    path('', views.Price, name="Gold_price")
]
