from django.shortcuts import render, HttpResponse
from django101.cities.models import Person


def index(req):
    context = {
        'name': 'MyName',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_phones(req):
    context = {
        'phones': [
            {
                'name': 'Galaxy s500',
                'quantity': 3,
            },
            {
                'name': 'iPhone 12',
                'quantity': 4,
            },
            {
                'name': 'Xiaomy Redmi 5',
                'quantity': 0,
            },
        ]
    }

    context['message'] = 'Phones list'

    return render(req, 'phones.html', context)
