__author__ = 'Carter'
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
import CHF.models as cMod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('CHF')

@view_function
def process_request(request):
    params = {}

    params['users'] = cMod.Client.objects.all()
    params['listForm'] = UserEditForm()
    params['User'] = ''

    if request.method == "POST":
        # UPDATE USER IF FORM IS VALID
        form = UserEditForm(request.POST)
        Client = cMod.Client()

        if form.is_valid():
            Client.first_name = form.cleaned_data['first_name']
            Client.last_name = form.cleaned_data['last_name']
            Client.email = form.cleaned_data['email']
            Client.username = form.cleaned_data['username']
            Client.save()
            Client.address = form.cleaned_data['address']
            Client.city = form.cleaned_data['city']
            Client.state = form.cleaned_data['state']
            Client.zip = form.cleaned_data['zip_code']
            Client.save()

            return HttpResponseRedirect('/CHF/ManageUsers')



    return templater.render_to_response(request, 'ManageUsers.html', params)


# EDIT USER FUNCTION
@view_function
def edit(request):
    params = {}

    try:
       User = cMod.Client.objects.get(id=request.urlparams[0])
    except cMod.Client.DoesNotExist:
        return HttpResponseRedirect('/CHF/ManageUsers')

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        print("FORMXXXXXXXXXXX:" + str(request.POST))

        # DELETE USER IF ARCHIVE WAS PRESSED
        if 'archiveButton' in request.POST:
            print("Archiving!")
            User.delete()
            return HttpResponseRedirect('/CHF/ManageUsers/')

        # UPDATE USER IF FORM IS VALID
        if form.is_valid():
            User.first_name = form.cleaned_data['first_name']
            print("XXXXXXXXXXXXX" + form.cleaned_data['first_name'])
            User.last_name = form.cleaned_data['last_name']
            User.address = form.cleaned_data['address']
            User.city = form.cleaned_data['city']
            User.state = form.cleaned_data['state']
            User.zip = form.cleaned_data['zip_code']
            User.email = form.cleaned_data['email']
            User.username = form.cleaned_data['username']
            User.save()
            User.save()
            print("Validated")
            # return HttpResponseRedirect('/CHF/ManageUsers/')

    # Generate Form Data
    params['User'] = User
    params['listForm'] = UserEditForm(initial={
        'first_name': User.first_name,
        'last_name': User.last_name,
        'address': User.address,
        'city': User.city,
        'state': User.state,
        'zip_code': User.zip,
        'username': User.username,
        'email': User.email,
    })

    # Get all user objects to populate list bar
    params['users'] = cMod.Client.objects.all()

    return templater.render_to_response(request, 'ManageUsers.html', params)


# CREATE USER FUNCTION
def create(request):
    params = {}

    User = cMod.Client()

    User.first_name = ''
    User.last_name = ''
    User.address = ''
    User.city = ''
    User.state = ''
    User.zip = ''
    User.email = ''
    User.username = ''

    params['users'] = cMod.Client.objects.all()
    params['listForm'] = UserEditForm(initial={
        'first_name': User.first_name,
        'last_name': User.last_name,
        'address': User.address,
        'city': User.city,
        'state': User.state,
        'zip_code': User.zip,
        'username': User.username,
        'email': User.email,
    })
    return templater.render_to_response(request, 'ManageUsers.html', params)


class UserEditForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    first_name = forms.CharField(required=True, max_length=25)
    last_name = forms.CharField(required=True, max_length=25)
    address = forms.CharField(required=True, max_length=25)
    city = forms.CharField(required=True, max_length=25)
    state = forms.CharField(required=True, max_length=2)
    zip_code = forms.CharField(required=True, max_length=25)
    email = forms.CharField(required=True, max_length=25)


