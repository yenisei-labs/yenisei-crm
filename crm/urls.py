from django.urls import path
from .views import get_deals, lists_api, list_api

urlpatterns = [
    path("deals/", get_deals, name="deals"),
    path("api/lists/", lists_api, name="lists_api"),
    path("api/lists/<int:pk>/", list_api, name="list_api"),
]
