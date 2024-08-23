from .views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='singup'),
    path('signin/', signin, name='singin'),
    path('signout/', signout, name='singout'),
    path('profile/', profile, name='profile'),
    path('shop/', include('Shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)