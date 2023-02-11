from django.urls import path
from .views import get_deals, list_api, new_deal, edit_deal, deal_order_api

urlpatterns = [
    path("deals/", get_deals, name="deals"),
    path("new-deal/", new_deal, name="new_deal"),
    path("edit-deal/<int:pk>/", edit_deal, name="edit_deal"),
    path("api/lists/<int:pk>/", list_api, name="list_api"),
    path("api/deals/<int:pk>/", deal_order_api, name="deal_order_api"),
]
