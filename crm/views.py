from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
    JsonResponse,
)
from django.contrib.auth.decorators import login_required
from .forms import DealListForm, DealForm, DealOrderForm, PersonForm
from .models import DealList, Deal, Person


@login_required
def redirect_to_deals(request) -> HttpResponse:
    return HttpResponseRedirect('/deals/')


@login_required
def get_deals(request) -> HttpResponse:
    """ The main page, url: /deals """
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

        return HttpResponseRedirect('/deals/')

    if request.method == 'GET':
        return handle_get_method()

    if request.method == 'POST':
        return handle_post_method()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def get_contacts(request) -> HttpResponse:
    """ Contacts, url: /contacts/ """
    def handle_get_method() -> HttpResponse:
        """ Returns html """
        return render(request, 'crm/contacts.html', {
            'people': Person.objects.all(),
            'form': PersonForm()
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

        return HttpResponseRedirect('/contacts/')

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
        submit_url = f"/deals/new/"

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

        return HttpResponseRedirect('/deals/')


    if request.method == 'GET':
        return handle_get_request()

    if request.method == 'POST':
        return handle_post_request()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def new_contact(request) -> HttpResponse:
    """ A page that allows to edit contacts """

    def handle_get_request() -> HttpResponse:
        """ Returns a form to submit a contact """
        contact_form = PersonForm(auto_id=False)
        submit_url = f"/contacts/new/"

        return render(request, 'crm/new-contact.html', {
            'contact_form': contact_form,
            'submit_url': submit_url,
        })

    def handle_post_request() -> HttpResponse:
        """ Handles form submission """
        form = PersonForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data
        person = Person(**form.cleaned_data)
        person.save()

        return HttpResponseRedirect('/contacts/')

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
        submit_url = f"/deals/edit/{pk}/"

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

        return HttpResponseRedirect('/deals/')

    if request.method == 'GET':
        return handle_get_request()

    if request.method == 'POST':
        return handle_post_request()

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def edit_contact(request, pk: int) -> HttpResponse:
    """ A page that allows to edit contacts """

    def handle_get_request() -> HttpResponse:
        """ Returns a form to submit changes """
        try:
            person = Person.objects.get(id=pk)
        except Person.DoesNotExist:
            return HttpResponseNotFound()

        contact_form = PersonForm(model_to_dict(person))
        submit_url = f"/contacts/edit/{pk}/"

        return render(request, 'crm/new-contact.html', {
            'contact_form': contact_form,
            'submit_url': submit_url,
        })

    def handle_post_request() -> HttpResponse:
        """ Handles form submission """
        try:
            person = Person.objects.get(id=pk)
        except Person.DoesNotExist:
            return HttpResponseNotFound()
        
        form = PersonForm(request.POST)
        if not form.is_valid():
            print(form.errors)
            return HttpResponseBadRequest()

        # process the data in form.cleaned_data
        for attr, value in form.cleaned_data.items():
            setattr(person, attr, value)
        person.save()

        return HttpResponseRedirect('/contacts/')

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


@login_required
def search_api(request, query: str) -> HttpResponse:
    deals = Deal.objects.filter(title__icontains=query)
    people = Person.objects.filter(first_name__icontains=query)

    results = []
    for deal in deals:
        results.append({
            'title': deal.title,
            'url': f'/deals/edit/{deal.id}/',
            'type': 'deal',
        })
    for person in people:
        results.append({
            'title': person.first_name,
            'url': f'/contacts/edit/{person.id}/',
            'type': 'contact',
        })

    return JsonResponse(results, safe=False)
