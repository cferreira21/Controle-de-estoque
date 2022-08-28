from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('mercadoria/', views.mercadoria, name='mercadoria'),
    path('mercadoria/delete/<pk>/', views.delete_mercadoria, name='delete_mercadoria'),
    path('mercadoria/update/<pk>/', views.update_mercadoria, name='update_mercadoria'),
]