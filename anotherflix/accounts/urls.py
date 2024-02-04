from django.urls import path
from . import views
from .views import LoginView 

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
