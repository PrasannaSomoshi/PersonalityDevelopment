from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('login', views.loginPage),
    path('logout', views.logoutUser),
    path('dashboard', views.dashboard),
    path('showTracker', views.showTracker),
    path('showReport', views.showReport),
]
