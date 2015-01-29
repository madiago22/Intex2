__author__ = 'Carter'
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import CHF.models as cMod
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('CHF')

@view_function
def process_request(request):
    params = {}

    params['users'] = cMod.Client.objects.all()

    return templater.render_to_response(request, 'ManageUsers.html',params)