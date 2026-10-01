from django.urls import path
from . import views

urlpatterns = [
   path('', views.landing_page, name='landing'),
    path('catalog/', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]