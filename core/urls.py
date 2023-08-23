from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.cadastro, name="cadastro"),
    path('login/', views.login_user, name="login"),
    path('painel/', views.painel, name="painel"),
    path('logout/', views.logout_user, name="logout"),
    path('pedidoform/', views.pedido_form, name="pedidoform"),
]