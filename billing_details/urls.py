from django.urls import path
from . import views
# from rest_framework import routers


# router = routers.
# router.register(r'billing_details', Billing_DetailsView)
# router.register(r'subscriptions', AddressView)

urlpatterns = [
    path('all/', views.Billing_detailsListView.as_view(), name=None),
    path('create/', views.Billing_detailsCreateView.as_view(), name=None),
    path('update/', views.Billing_detailsUpdateView.as_view(), name=None)
]