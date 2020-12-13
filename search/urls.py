from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addVideo/', views.addVideo),
    path('results/', views.searchResults),
]
