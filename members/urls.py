from django.urls import path
from members import views

urlpatterns = [
  path('register/', views.UserRegisterView.as_view(), name='register'),
  # path('login/', views.UserRegisterView.as_view(), name='login'),
]

