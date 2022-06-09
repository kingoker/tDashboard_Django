from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('order/<int:pk>', views.order, name='order'),
    path('rating', views.rating, name='rating'),
    path('profile', views.profile, name='profile'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]