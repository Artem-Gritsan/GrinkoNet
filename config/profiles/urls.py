from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.ListUsers.as_view()),
    path('users/<int:pk>/', views.UserNetPublicView.as_view()),
    path('users/me/', views.UserNetView.as_view()),
]

