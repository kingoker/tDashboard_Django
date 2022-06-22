from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('order/<int:pk>', views.order, name='order'),
    path('products/<int:pk>', views.products, name='products'),
    path('orderproducts/<int:pk>/<int:id>', views.orderproducts, name='orderproducts'),
    path('rating', views.rating, name='rating'),
    path('profile', views.profile, name='profile'),
    path('company/<int:pk>', views.company, name='company'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]