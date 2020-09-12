from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base),
    path('login', views.user_login),
    path('register', views.register),
    path('success', views.success),
    path('logout', views.logout_request),
    path('', include('django.contrib.auth.urls')),
]
