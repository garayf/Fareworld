from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('resume/', views.card_page_resume, name='resume'),
    path('', views.card_page_landing, name='landing')
    
]
