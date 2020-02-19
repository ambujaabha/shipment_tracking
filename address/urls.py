from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressListView.as_view(), name=None),
    path('create/', views.AddressCreateView.as_view(), name=None),
    path('update/', views.AddressUpdateView.as_view(), name=None),
]