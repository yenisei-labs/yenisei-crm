from django.urls import path
from .views import get_deals, lists_api, list_api, new_deal

urlpatterns = [
    path("deals/", get_deals, name="deals"),
    path("new-deal/", new_deal, name="new_deal"),
    path("api/lists/", lists_api, name="lists_api"),
    path("api/lists/<int:pk>/", list_api, name="list_api"),
]
