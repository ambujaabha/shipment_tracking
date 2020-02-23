from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name=None),
    path('create/', views.OrderCreateView.as_view(), name=None),
    path('update/', views.OrderUpdateView.as_view(), name=None)
]