from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_list, name='students_list')
]