from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('list/', views.list_tales, name='list_tales'),
    path('', views.landing_page, name='landing_page'),
    path('add/', views.add_tale, name='add_tale'),       
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
