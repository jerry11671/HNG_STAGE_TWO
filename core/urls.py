from django.urls import path
from .views import UserGetCreate

urlpatterns = [
    path('api/', UserGetCreate.as_view(), name='user_create'),
    path('api/<str:pk>/', UserGetCreate.as_view(), name='user_detail'),
]