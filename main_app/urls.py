from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('routers/', views.RouterList.as_view(), name='router_list'),
    path('switchs/', views.RouterList.as_view(), name='switch_list'),
]