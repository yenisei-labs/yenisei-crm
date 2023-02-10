from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import DealListForm
from .models import DealList

@login_required
def get_deals(request):
    deal_lists = DealList.objects.all()
    new_deal_form = DealListForm()
    return render(request, 'crm/deals.html', {
        'new_deal_form': new_deal_form,
        'deal_lists': deal_lists
    })

@login_required
def deals_api(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DealListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            deal_list = DealList(title=title)
            deal_list.save()
            return HttpResponseRedirect('/crm/deals/')
