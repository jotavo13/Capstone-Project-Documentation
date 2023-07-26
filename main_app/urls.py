from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('routers/', views.RouterList.as_view(), name='router_list'),
    path('routers/new', views.RouterCreate.as_view(), name='router_create'),
    path('routers/<int:pk>/', views.RouterDetail.as_view(), name='router_detail'),
    path('routers/<int:pk>/update', views.RouterUpdate.as_view(), name='router_update'),
    path('routers/<int:pk>/delete', views.RouterDelete.as_view(), name='router_delete'),
    path('switches/', views.SwitchList.as_view(), name='switch_list'),
    path('switches/new', views.SwitchCreate.as_view(), name='switch_create'),
    path('switches/<int:pk>/', views.SwitchDetail.as_view(), name='switch_detail'),
    path('switches/<int:pk>/update', views.SwitchUpdate.as_view(), name='switch_update'),
    path('switches/<int:pk>/delete', views.SwitchDelete.as_view(), name='switch_delete'),
    path('documentations/', views.DocumentationList.as_view(), name='documentation_list'),
    path('documentations/new', views.DocumentationCreate.as_view(), name='documentation_create'),
    path('documentations/<int:pk>/', views.DocumentationDetail.as_view(), name='documentation_detail'),
    path('documentations/<int:pk>/update', views.DocumentationUpdate.as_view(), name='documentation_update'),
    path('documentations/<int:pk>/delete', views.DocumentationDelete.as_view(), name='documentation_delete'),

]