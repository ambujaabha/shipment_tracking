from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShipmentListView.as_view(), name=None),
    path('create/', views.ShipmentCreateView.as_view(), name=None),
    path('update/', views.ShipmentUpdateView.as_view(), name=None),