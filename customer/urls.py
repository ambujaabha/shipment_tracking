from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name=None),
    path('create/', views.CustomerCreateView.as_view(), name=None),
    path('update/', views.CustomerUpdateView.as_view(), name=None)
]