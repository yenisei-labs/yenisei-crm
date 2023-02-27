from django.urls import path
from .views import (
    redirect_to_deals,
    get_deals, get_contacts,
    new_deal, new_contact,
    edit_deal, delete_deal, edit_contact,
    list_api, deal_order_api, search_api,
)

urlpatterns = [
    path("", redirect_to_deals, name="redirect_to_deals"),
    path("deals/", get_deals, name="deals"),
    path("deals/new/", new_deal, name="new_deal"),
    path("deals/edit/<int:pk>/", edit_deal, name="edit_deal"),
    path("deals/delete/<int:pk>/", delete_deal, name="delete_deal"),
    path("contacts/", get_contacts, name="contacts"),
    path("contacts/new/", new_contact, name="new_contact"),
    path("contacts/edit/<int:pk>/", edit_contact, name="edit_contact"),
    path("api/lists/<int:pk>/", list_api, name="list_api"),
    path("api/order/<int:pk>/", deal_order_api, name="deal_order_api"),
    path("api/search/<str:query>/", search_api, name="search"),
]
