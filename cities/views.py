from django.shortcuts import render
from cities.models import Person


def index(req):
    context = {
        'name': 'MyName',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
