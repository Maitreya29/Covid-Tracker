from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('country/<country>/', views.info),
    path('country/<country>', views.info),
]
