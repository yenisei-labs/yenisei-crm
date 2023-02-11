from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from .forms import DealListForm, DealForm
from .models import DealList

@login_required
def get_deals(request):
    deal_lists = DealList.objects.all()
    deal_list_form = DealListForm()
    return render(request, 'crm/deals.html', {
        'new_deal_form': deal_list_form,
        'deal_lists': deal_lists
    })


@login_required
def new_deal(request):
    try:
        list_id = request.GET['list']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        deal_list = DealList.objects.get(id=list_id)
    except DealList.DoesNotExist:
        return HttpResponseNotFound()

    deal_form = DealForm()

    return render(request, 'crm/new-deal.html', {
        'deal_list': deal_list,
        'deal_form': deal_form,
    })


@login_required
def lists_api(request) -> HttpResponse:
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DealListForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data as required
        title = form.cleaned_data['title']
        deal_list = DealList(title=title)
        deal_list.save()
        return HttpResponseRedirect('/crm/deals/')
    return HttpResponseNotAllowed(['POST'])


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
