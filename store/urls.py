from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit profile'),
    path('change_password/', views.change_password, name='change password'),

]