from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransportListView.as_view(), name=None),
    path('create/', views.TransportCreateView.as_view(), name=None),
    path('update/', views.TransportUpdateView.as_view(), name=None)
]