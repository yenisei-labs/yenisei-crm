from django.urls import path
from .views import get_deals, deals_api

urlpatterns = [
    path("deals/", get_deals, name="deals"),
    path("api/deals/", deals_api, name="deals_api")
]
