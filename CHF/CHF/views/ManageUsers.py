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

    return templater.render_to_response(request, 'ManageUsers.html', params)

@view_function
def edit(request):
    params = {}
    params['users'] = cMod.Client.objects.all()
    try:
       User = cMod.Client.objects.get(id=request.urlparams[0])
    except cMod.Client.DoesNotExist:
        return HttpResponseRedirect('/CHF/ManageUsers')

    params['User'] = User
    form = UserEditForm(initial={
        'first_name': User.user.first_name,
        'email': User.user.email,
        'last_name': User.user.last_name,
    })
    params['form'] = form

    return templater.render_to_response(request, 'ManageUsers.html', params)


class UserEditForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=25)
    last_name = forms.CharField(required=True, max_length=25)
    email = forms.CharField(required=True, max_length=25)