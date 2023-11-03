from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_csv),   
    path('null/', views.read_csv_null),
    path('avg/', views.age_avg),
    path('avg2/', views.avg_age2),
]