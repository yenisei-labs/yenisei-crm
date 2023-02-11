from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from .forms import DealListForm, DealForm, DealOrderForm
from .models import DealList, Deal

@login_required
def get_deals(request) -> HttpResponse:
    """ The main page, url: /crm/deals """
    def handle_get_method() -> HttpResponse:
        """ Returns html """
        deal_lists = DealList.objects.all()
        deal_list_form = DealListForm()
        deals_without_list = Deal.objects.filter(list=None)
        
        return render(request, 'crm/deals.html', {
            'new_deal_form': deal_list_form,
            'deal_lists': deal_lists,
            'deals_without_list': deals_without_list,
        })
    
    def handle_post_method() -> HttpResponse:
        """ Handles list form submission """
        form = DealListForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data
        title = form.cleaned_data['title']
        deal_list = DealList(title=title)
        deal_list.save()

        return HttpResponseRedirect('/crm/deals/')

    if request.method == 'GET':
        return handle_get_method()

    if request.method == 'POST':
        return handle_post_method()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def new_deal(request) -> HttpResponse:
    """ A page that allows to create new deals """

    def handle_get_request() -> HttpResponse:
        """ Returns a form to submit a new deal """
        try:
            list_id = request.GET['list']
            deal_list = DealList.objects.get(id=list_id)
        except KeyError:
            deal_list = DealList.objects.first()
        except DealList.DoesNotExist:
            return HttpResponseNotFound()

        deal_form = DealForm(auto_id=False)
        submit_url = f"/crm/new-deal/"

        return render(request, 'crm/new-deal.html', {
            'deal_list': deal_list,
            'deal_form': deal_form,
            'submit_url': submit_url,
        })

    def handle_post_request() -> HttpResponse:
        """ Handles form submission """
        form = DealForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data
        deal = Deal(**form.cleaned_data)
        deal.save()

        return HttpResponseRedirect('/crm/deals/')

    if request.method == 'GET':
        return handle_get_request()

    if request.method == 'POST':
        return handle_post_request()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def edit_deal(request, pk: int) -> HttpResponse:
    """ A page that allows to edit deals """

    def handle_get_request() -> HttpResponse:
        """ Returns a form to submit changes """
        try:
            deal = Deal.objects.get(id=pk)
        except Deal.DoesNotExist:
            return HttpResponseNotFound()

        deal_form = DealForm(model_to_dict(deal))
        submit_url = f"/crm/edit-deal/{pk}/"

        return render(request, 'crm/new-deal.html', {
            'deal_form': deal_form,
            'submit_url': submit_url,
        })

    def handle_post_request() -> HttpResponse:
        """ Handles form submission """
        try:
            deal = Deal.objects.get(id=pk)
        except Deal.DoesNotExist:
            return HttpResponseNotFound()
        
        form = DealForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data
        for attr, value in form.cleaned_data.items():
            setattr(deal, attr, value)
        deal.save()

        return HttpResponseRedirect('/crm/deals/')

    if request.method == 'GET':
        return handle_get_request()

    if request.method == 'POST':
        return handle_post_request()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def list_api(request, pk: int) -> HttpResponse:
    # Formally, this is instead of a PATCH request.
    # I couldn't find a way to get the data from the PATCH request.
    def handle_post_request() -> HttpResponse:
        try:
            deal_list = DealList.objects.get(id=pk)
        except DealList.DoesNotExist:
            return HttpResponseNotFound()
        
        form = DealListForm(request.POST)
        # check whether the form is valid:
        if not form.is_valid():
            return HttpResponseBadRequest()
        
        # process the data in form.cleaned_data as required
        title = form.cleaned_data['title']
        deal_list.title = title
        deal_list.save()

        response = HttpResponse()
        response.status_code = 200
        return response

    def handle_delete_request() -> HttpResponse:
        try:
            deal_list = DealList.objects.get(id=pk)
        except DealList.DoesNotExist:
            return HttpResponseNotFound()

        deal_list.delete()
        response = HttpResponse()
        response.status_code = 200
        return response

    if request.method == 'POST':
        return handle_post_request()

    if request.method == 'DELETE':
        return handle_delete_request()

    return HttpResponseNotAllowed(['POST', 'DELETE'])


@login_required
def deal_order_api(request, pk: int) -> HttpResponse:
    # Formally, this is instead of a PATCH request.
    # I couldn't find a way to get the data from the PATCH request.
    def handle_post_request() -> HttpResponse:
        try:
            deal = Deal.objects.get(id=pk)
        except Deal.DoesNotExist:
            return HttpResponseNotFound()
        
        form = DealOrderForm(request.POST)
        # check whether the form is valid:
        if not form.is_valid():
            return HttpResponseBadRequest()
        
        # process the data in form.cleaned_data as required
        order = form.cleaned_data['order']
        deal_list = form.cleaned_data['list']
        deal.order = order
        deal.list = deal_list
        deal.save()

        response = HttpResponse()
        response.status_code = 200
        return response

    if request.method == 'POST':
        return handle_post_request()

    return HttpResponseNotAllowed(['POST'])
