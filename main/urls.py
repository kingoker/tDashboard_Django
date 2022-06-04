from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.sell, name='home'),
    path('rating', views.rating, name='rating'),
    path('buy', views.buy, name='buy'),
    path('profile', views.profile, name='profile'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]