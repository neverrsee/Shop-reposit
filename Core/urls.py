from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='singup'),
    path('signin/', signin, name='singin'),
    path('signout/', signout, name='singout'),
    path('profile/', profile, name='profile'),
]