from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.list_announcements, name='announcement_list'),
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),  
]
