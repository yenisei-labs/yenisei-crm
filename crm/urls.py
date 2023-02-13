from django.urls import path
from .views import (
    get_deals, get_contacts,
    new_deal, new_contact,
    edit_deal, edit_contact,
    list_api, deal_order_api,
)

urlpatterns = [
    path("deals/", get_deals, name="deals"),
    path("new-deal/", new_deal, name="new_deal"),
    path("edit-deal/<int:pk>/", edit_deal, name="edit_deal"),
    path("contacts/", get_contacts, name="contacts"),
    path("contacts/new/", new_contact, name="new_contact"),
    path("contacts/edit/<int:pk>/", edit_contact, name="edit_contact"),
    path("api/lists/<int:pk>/", list_api, name="list_api"),
    path("api/deals/<int:pk>/", deal_order_api, name="deal_order_api"),
]
