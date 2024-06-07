# create urlpatterns for accounts app
from django.urls import path
from accounts import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'), # path /accounts/registerUser/ will call registerUser function in views.py
]
