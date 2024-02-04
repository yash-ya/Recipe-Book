from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login, name='login'),
    path('user/logout/<str:user_id>/', views.logout, name='logout')
]
