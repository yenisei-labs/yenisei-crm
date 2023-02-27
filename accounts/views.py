from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LogInForm


def log_in(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/deals/')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/accounts/login/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LogInForm()

    return render(request, 'accounts/login.html', {'form': form})
