from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('resume/', views.card_page_resume, name='resume'),
    path('', views.card_page_landing, name='landing')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
